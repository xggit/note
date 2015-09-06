# LUA 加密

## luac加密

使用luac编译为字节码，可以实现加密

```lua
-- 将lang.lua生成out.lua
luac -o out.lua lang.lua
```

## luajit加密

使用lua原生的加密，在cocos2d-x中使用不了，它里面使用的luajit.

luajit -b [脚本名] [编译后的脚本名]

## Cocos2d-x集成的加密xxtea

3.x版本将加密默认集成了（cocos2d-x\external\xxtea）

```
cocos luacompile -v -s ./src -d ./src_luac -e -k key_name -b sign_name
```

