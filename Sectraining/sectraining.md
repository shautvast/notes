sec training notes

### Cross-Site Scripting

#### Content Security Policy (CSP)
For example:
`Content-Security-Policy: default-src: 'self'; script-src: 'self' static.domain.tld`

The above CSP will instruct the web browser to load all resources only from the page's origin and JavaScript source code files from static.domain.tld. For more details on the Content Security Policy, including what it does and how to use it, see this article.


#### X-XSS-Protection Header
This HTTP response header enables the Cross-Site Scripting (XSS) filter built into some modern web browsers. The header is usually enabled by default anyway, so its role is to re-enable the filter for a particular website if the user disabled it.

#### Content Types
To prevent non-HTML HTTP responses from embedding data, that might be dangerously interpreted as HTML or JavaScript, it is recommended to always send the Content-Type header in the HTTP response to ensure that browsers interpret it in the way it's intended.

#### Modern Frameworks
JavaScript frameworks (e.g., Angular, React) or server-side templating systems (e.g., Go Templates) have robust built-in protections against Reflected Cross-Site Scripting.

#### Java

|context|vulnerable code | java |
|---|---|---|
|HTML Body	|&lt;div>USER-CONTROLLED-DATA</div>	| `Encode.forHtml` |
|HTML Attribute|	&lt;input type="text" value="USER-CONTROLLED-DATA">	|`Encode.forHtmlAttribute`|
|URL Parameter|	&lt;a href="/search?value=USER-CONTROLLED-DATA">Search</a>	|`Encode.forUriComponent`|
|CSS String	|&lt;div style="width: USER-CONTROLLED-DATA;">Selection</div>|	`Encode.forCssString`|
|CSS URL|	&lt;div style="background: USER-CONTROLLED-DATA ">	|`Encode.forCssUrl`|
|JavaScript Block	|&lt;script>alert("USER-CONTROLLED-DATA")</script>|	`Encode.forJavaScriptBlock`|
|JavaScript Variable	|&lt;button onclick="alert('USER-CONTROLLED-DATA');">click me</button>	|`Encode.forJavaScriptVariable`|

### Cross-Site Request Forgery
#### Prevention

[synchronizer token pattern](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#synchronizer-token-pattern)

A number of code patterns that prevent CSRF attacks exist, and more than one can be applied at the same time as part of a defence in depth security strategy.

Developers should require anti-forgery tokens for any unsafe methods (POST, PUT, DELETE) and ensure that safe methods (GET, HEAD) do not have any side effects.

Developers should consider implementing a Synchronizer Token Pattern:

A random token is generated server-side upon successful authentication and associated with the user's session. The token is returned to the user as part of an HTML response (e.g. a hidden field in a form or retrieved by AJAX).

When the user needs to perform a sensitive operation, the token is included in the request. The application verifies the correctness of the token, and then performs the requested action only if the token in the request matches the token stored in the user's session.

If maintaining the state for a CSRF token at the server side is problematic, developers can adopt the Double Submit Cookie Pattern. This is an easy to implement, stateless alternative that assigns a random value to both a cookie, and a request parameter, with the server verifying if the cookie value and request value match:

The client requests an HTML page that contains a form.
The server includes two tokens in the response. One token is sent as a cookie. The other is placed in a hidden form field. The tokens are generated randomly so that an adversary cannot guess the values.
When the client submits the form, it must send both tokens back to the server. The client sends the cookie token as a cookie, and it sends the form token inside the form data.
If a request does not include both tokens, the server disallows the request.
If the origin header is present, developers should verify that its value matches the target origin. Unlike the Referer, the Origin header will be present in HTTP requests that originate from an HTTPS URL.

If the origin header is not present, developers should verify that the hostname in the Referer header matches the target origin. This method of CSRF mitigation is also commonly used with unauthenticated requests, such as requests made prior to establishing a session state, which is required to keep track of a synchronization token.

Importantly, developers should enforce User Interaction based CSRF Defense:

Re-Authentication (password or stronger)
One-time Token
CAPTCHA

```java
public class CSRF {
	public static String getToken() throws NoSuchAlgorithmException{
	    // generate random data
	    SecureRandom secureRandom = SecureRandom.getInstance("SHA1PRNG");
	    byte[] data = new byte[16];
	    secureRandom.nextBytes(data);

	    // convert to Base64 string
	    return Base64.getEncoder().encodeToString(data);
	}
}
```

```jsp
<%
// generate a random CSRF token
String csrfToken = CSRF.getToken();

// place the CSRF token in a cookie
javax.servlet.http.Cookie cookie = new javax.servlet.http.Cookie("csrf", csrfToken);
response.addCookie(cookie);
%>

<form action="/action" method="POST">
  <input type="hidden" name="csrfToken" value="<%= csrfToken %>"/>
</form>
```

```java
public void doAction(HttpServletRequest request, HttpServletResponse response) {
	// get the CSRF cookie
	String csrfCookie = null;
	for (Cookie cookie : request.getCookies()) {
		if (cookie.getName().equals("csrf")) {
			csrfCookie = cookie.getValue();
		}
	}

	// get the CSRF form field
	String csrfField = request.getParameter("csrfToken");

	// validate CSRF
	if (csrfCookie == null || csrfField == null || !csrfCookie.equals(csrfField)) {
		try {
			response.sendError(401);
		} catch (IOException e) {
			// ...
		}
		return;
	}

	// ...
}
```

### Open Redirect

#### Java Prevention
Unless the development is aided by third-party libraries, developers must implement their own solution to determine whether the user-controlled string represents a local path or not. If the list of permitted URLs for redirection is known, implement an allow list of such URLs.

Otherwise, an easy ad hoc solution could be the following:
```java
private static boolean isLocal(String path) {
    return path.startsWith("/") && !path.startsWith("//");
}
```

### Broken Authorization

#### prevention in java (spring boot)

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity security) throws Exception {
        http
          .authorizeRequests()
          .antMatchers("/admin/**").hasRole("ROLE_ADMIN");
    }
    ...
}
```

and

```java
@Service
public class AdminService {
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public List<Organization> findAllOrganizations() { ... }
    ...
}
```


### Server-Side Request Forgery

Vulnerable Example

```java
private static String fetchRemoteObject(String location) throws Exception {
    URL url = new URL(location);
    URLConnection connection = url.openConnection();
    BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
    String body = reader.lines().collect(Collectors.joining());
    return body;
}
```

#### solution

```java
private static String fetchRemoteObject(String location) throws Exception {
    URL url = new URL(location);

    if (!url.getHost().endsWith(".example.com") ||
        !url.getProtocol().equals("http") &&
        !url.getProtocol().equals("https")) {
        throw new Exception("Forbidden remote source");
    }

    URLConnection connection = url.openConnection();
    BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
    String body = reader.lines().collect(Collectors.joining());
    return body;
}
```

### XML Entity Expansion

#### billion laughs attack
```xml
<?xml version="1.0" encoding="ISO-8859-1"?> 
<!DOCTYPE foo [
  <!ELEMENT foo ANY>
  <!ENTITY bar "SecureFlag ">
  <!ENTITY t1 "&bar;&bar;">
  <!ENTITY t2 "&t1;&t1;&t1;&t1;">
  <!ENTITY t3 "&t2;&t2;&t2;&t2;&t2;">
]>
<foo>
  Join &t3;
</foo>
```

#### forgery
```xml
<?xml version="1.0" encoding="ISO-8859-1"?> 
<!DOCTYPE foo [
  <!ELEMENT foo ANY>
  <!ENTITY xxe SYSTEM
  "file:///etc/passwd">
]>
<foo>
  &xxe;
</foo>
```

or 

```xml
<?xml version="1.0" encoding="ISO-8859-1"?> 
<!DOCTYPE foo [
  <!ELEMENT foo ANY>
  <!ENTITY xxe SYSTEM
  "http://internal.vulnerableapp.com:8443">
]>
<foo>
  &xxe;
</foo>
```

_Just who invented these unnecessary attack vectors_ Or was this deemed useful at the time? I certainly never used it, or thought this would come in handy...

#### Prevention

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
String FEATURE = null;
try {
    FEATURE = "http://apache.org/xml/features/disallow-doctype-decl";
    dbf.setFeature(FEATURE, true);

    FEATURE = "http://xml.org/sax/features/external-general-entities";
    dbf.setFeature(FEATURE, false);

    FEATURE = "http://xml.org/sax/features/external-parameter-entities";
    dbf.setFeature(FEATURE, false);

    FEATURE = "http://apache.org/xml/features/nonvalidating/load-external-dtd";
    dbf.setFeature(FEATURE, false);

    dbf.setXIncludeAware(false);
    dbf.setExpandEntityReferences(false);
   
} catch (ParserConfigurationException e) {
    logger.info("ParserConfigurationException was thrown. The feature '" + FEATURE 
    + "' is probably not supported by your XML processor.");
} catch (SAXException e) {
    logger.warning("A DOCTYPE was passed into the XML document");
} catch (IOException e) {
    logger.error("IOException occurred, XXE may still possible: " + e.getMessage());
}

// Load XML file or stream using a XXE agnostic configured parser
DocumentBuilder safebuilder = dbf.newDocumentBuilder();
```

#### XMLInputFactory (a StAX parser)

```java
xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, false); 
// disable external entities
xmlInputFactory.setProperty("javax.xml.stream.isSupportingExternalEntities", false);
```

#### TransformerFactory

```java
TransformerFactory tf = TransformerFactory.newInstance();
tf.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
tf.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
```

#### Validator

```java
SchemaFactory factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
Schema schema = factory.newSchema();
Validator validator = schema.newValidator();
validator.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
validator.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
```

#### SchemaFactory

```java
SchemaFactory factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
Schema schema = factory.newSchema(Source);
```

#### SAXTransformerFactory

```java
SAXTransformerFactory sf = SAXTransformerFactory.newInstance();
sf.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
sf.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
sf.newXMLFilter(Source);
```

1. javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD
2. javax.xml.XMLConstants.ACCESS_EXTERNAL_SCHEMA
3. javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET

#### XMLReader

```java
XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
// This may not be strictly required as DTDs shouldn't be allowed at all, per previous line.
reader.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false); 
reader.setFeature("http://xml.org/sax/features/external-general-entities", false);
reader.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

#### SAXReader

```java
saxReader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
saxReader.setFeature("http://xml.org/sax/features/external-general-entities", false);
saxReader.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

#### SAXBuilder

```java
SAXBuilder builder = new SAXBuilder();
builder.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);
builder.setFeature("http://xml.org/sax/features/external-general-entities", false);
builder.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
Document doc = builder.build(new File(fileName));
```

No-op EntityResolver
For APIs that take an EntityResolver, you can neutralize an XML parser's ability to resolve entities by supplying a no-op implementation:

```java
public final class NoOpEntityResolver implements EntityResolver {
    public InputSource resolveEntity(String publicId, String systemId) {
        return new InputSource(new StringReader(""));
    }
}

xmlReader.setEntityResolver(new NoOpEntityResolver());
documentBuilder.setEntityResolver(new NoOpEntityResolver());
```

#### JAXB Unmarshaller

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature("http://xml.org/sax/features/external-general-entities", false);
spf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
spf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);

//Do unmarshall operation
Source xmlSource = new SAXSource(spf.newSAXParser().getXMLReader(), 
                                new InputSource(new StringReader(xml)));
JAXBContext jc = JAXBContext.newInstance(Object.class);
Unmarshaller um = jc.createUnmarshaller();
um.unmarshal(xmlSource);
```

#### XPathExpression

```java
DocumentBuilderFactory df = DocumentBuilderFactory.newInstance();
df.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
df.setAttribute(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
DocumentBuilder builder = df.newDocumentBuilder();
String result = new XPathExpression().evaluate( builder.parse(
                            new ByteArrayInputStream(xml.getBytes())) );
java.beans.XMLDecoder
The readObject() method in this class is fundamentally unsafe. Not only is the XML it parses subject to XXE, but the method can be used to construct any Java object, and execute arbitrary code as described here. Importantly, there is no way to make safe use of this class except to trust or properly validate the input being passed into it. As such, we strongly recommend completely avoiding the use of this class and replacing it with a safe or properly configured XML parser as described elsewhere in this cheat sheet.
```

#### Spring Framework MVC/OXM XXE Vulnerabilities

For example, some XXE vulnerabilities were found in Spring OXM and Spring MVC. The following versions of the Spring Framework are vulnerable to XXE:

3.0.0 to 3.2.3 (Spring OXM & Spring MVC)
4.0.0.M1 (Spring OXM)
4.0.0.M1-4.0.0.M2 (Spring MVC)
There were other issues as well that were fixed later, so to fully address these issues, Spring recommends you upgrade to Spring Framework 3.2.8+ or 4.0.2+.
For Spring OXM, this is referring to the use of org.springframework.oxm.jaxb.Jaxb2Marshaller. Note that the CVE for Spring OXM specifically indicates that 2 XML parsing situations are up to the developer to get right, and 2 are the responsibility of Spring and were fixed to address this CVE.
Here's what they say:
Two situations developers must handle:

For a DOMSource, the XML has already been parsed by user code, and that code is responsible for protecting against XXE.
For a StAXSource, the XMLStreamReader has already been created by user code, and that code is responsible for protecting against XXE.
The issue Spring fixed:
For SAXSource and StreamSource instances, Spring processed external entities by default, thereby creating this vulnerability.
Here's an example of using a StreamSource that was vulnerable, but is now safe, if you are using a fixed version of Spring OXM or Spring MVC:

```java
import org.springframework.oxm.Jaxb2Marshaller;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;

Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
// Must cast return Object to whatever type you are unmarshalling
marshaller.unmarshal(new StreamSource(new StringReader(some_string_containing_XML));
```

### Unsafe Deserialization

#### prevention

```java
ObjectInputStream objectInputStream = new ObjectInputStream(buffer);
stream.setObjectInputFilter(MyFilter::myFilter);
```

together with

```java
public class MyFilter {
    static ObjectInputFilter.Status myFilter(ObjectInputFilter.FilterInfo info) {
        Class<?> serialClass = info.serialClass();
        if (serialClass != null) {
            return serialClass.getName().equals(MyClass.class.getName())
                    ? ObjectInputFilter.Status.ALLOWED
                    : ObjectInputFilter.Status.REJECTED;
        }
        return ObjectInputFilter.Status.UNDECIDED;
    }
}
```

OR

```java
public class MyFilteringInputStream extends ObjectInputStream {
    public MyFilteringInputStream(InputStream inputStream) throws IOException {
        super(inputStream);
    }

    @Override
    protected Class<?> resolveClass(ObjectStreamClass objectStreamClass) throws IOException, ClassNotFoundException {
        if (!objectStreamClass.getName().equals(MyClass.class.getName())) {
            throw new InvalidClassException("Forbidden class", objectStreamClass.getName());
        }
        return super.resolveClass(objectStreamClass);
    }
}
```
