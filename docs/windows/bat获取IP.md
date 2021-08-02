# bat获取IP

```batch
FOR /F "tokens=4" %%i IN ('route print^|findstr 0.0.0.0.*0.0.0.0') DO (SET IP=%%i)
ECHO %IP%
```
