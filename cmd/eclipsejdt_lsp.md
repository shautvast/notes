java -jar plugins/org.eclipse.equinox.launcher_1.6.700.v20231214-2017.jar \\
  -Declipse.application=org.eclipse.jdt.ls.core.id1 \\
  -Dosgi.bundles.defaultStartLevel=4 \\
  -Declipse.product=org.eclipse.jdt.ls.core.product \\
  -Dlog.level=ALL \\
  -Xmx1G \\
  --add-modules=ALL-SYSTEM \\
  --add-opens java.base/java.util=ALL-UNNAMED \\
  --add-opens java.base/java.lang=ALL-UNNAMED \\
  -configuration ./config_mac \\
  -data .

  \# -data needs local workspace
  
