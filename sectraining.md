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
