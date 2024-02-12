```bash
java -jar plugins/org.eclipse.equinox.launcher_1.6.700.v20231214-2017.jar \
  -Declipse.application=org.eclipse.jdt.ls.core.id1 \
  -Dosgi.bundles.defaultStartLevel=4 \
  -Declipse.product=org.eclipse.jdt.ls.core.product \
  -Dlog.level=ALL \
  -Xmx1G \
  --add-modules=ALL-SYSTEM \
  --add-opens java.base/java.util=ALL-UNNAMED \
  --add-opens java.base/java.lang=ALL-UNNAMED \
  -configuration ./config_mac \
  -data .
```
  \# -data needs local workspace
  
```rust
OsString::from("-jar"),
OsString::from("/../jdt-language-server-1.31.0-202401111522/plugins/org.eclipse.equinox.launcher_1.6.700.v20231214-2017.jar"),
OsString::from("-Declipse.application=org.eclipse.jdt.ls.core.id1"),
OsString::from("-Dosgi.bundles.defaultStartLevel=4"),
OsString::from("-Declipse.product=org.eclipse.jdt.ls.core.product"),
OsString::from("-Dlog.level=ALL"),
OsString::from("-Xmx1G"),
OsString::from("--add-modules=ALL-SYSTEM"),
OsString::from("--add-opens"),
OsString::from("java.base/java.util=ALL-UNNAMED"),
OsString::from("--add-opens java.base/java.lang=ALL-UNNAMED"),
OsString::from("-configuration"),
OsString::from("/../jdt-language-server-1.31.0-202401111522/config_mac_arm"),
OsString::from("-data"),
OsString::from("{project}"),
```
