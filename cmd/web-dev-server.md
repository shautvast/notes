start server with reload

`wds -c web-demo-server.config.mjs --watch`

Who would have though that the mocks that were setup used cookies to communicate with the client
So I had to resort to deleting them because otherwise the cookies of the previous run were still in.
After the reset new values are probably used. TODO verify that.

I took out the customer specifics here (middleware)

```javascript
import ...

/// removing the cookies makes sure the mocks work allright
const removeCookies = () => {
  return async (context, next) => {
    // console.log(context); // can be turned on for debugging
    context.request.header.cookie="";
    return next();
  };
};

export default {
  open: 'demo',
  nodeResolve: true,
  middleware: [
    removeCookies(),
  ]
};

```
