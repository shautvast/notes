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
