# 为程序写自动测试脚本
---

## 脚本案例

+ 为程序开启时频率闪退写自动测试脚本

```bash
#!/bin/bash
for((i=1;i<500;i++))
do
    adb shell am start com.togic.gamecenter/.GameCenter
    sleep 10
    adb shell input keyevent 4
    sleep 5
    echo $i
done

```

+ 使用adb logcat 获取关键字上下文打印信息

```bash
adb logcat -c && adb logcat | grep -C 80 -B 80 "Build fingerprint" > crash_log.txt
```

android ndk时crash位置会有关键词”Build fingerprint”, -C 80 -B 80是上下80行打印都输出


