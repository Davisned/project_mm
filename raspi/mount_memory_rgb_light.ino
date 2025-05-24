// PINs gemäß Deinem Wiring-Diagramm
const int PIN_RED   = 23;
const int PIN_GREEN = 22;
const int PIN_BLUE  = 21;

void setup() {
  Serial.begin(115200);

  // PWM-Ausgabe aktivieren (pinMode für analogWrite nicht nötig, aber schadet nicht)
  pinMode(PIN_RED,   OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE,  OUTPUT);
}

void loop() {
  // warten, bis über Seriell 3 Werte R,G,B hereinkommen im Format "255,128,0\n"
  if (!Serial.available()) return;

  String line = Serial.readStringUntil('\n');
  line.trim();
  if (line.length()==0) return;

  // String in drei Ganzzahlen zerlegen
  int v[3] = {0,0,0}, idx = 0;
  char *buf = strdup(line.c_str());
  char *tok = strtok(buf, ",");
  while (tok && idx<3) {
    v[idx++] = atoi(tok);
    tok = strtok(NULL, ",");
  }
  free(buf);
  if (idx<3) return;  // nicht genug Werte gekommen

  // Grenzwerte einhalten
  uint8_t r = constrain(v[0], 0, 255);
  uint8_t g = constrain(v[1], 0, 255);
  uint8_t b = constrain(v[2], 0, 255);

  // PWM-Ausgabe
  analogWrite(PIN_RED,   r);
  analogWrite(PIN_GREEN, g);
  analogWrite(PIN_BLUE,  b);
}