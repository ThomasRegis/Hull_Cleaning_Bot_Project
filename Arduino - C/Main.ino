  int MoteurdroiteDIR1 = 10;
  int MoteurdroitePW1 = 9;
  int  MoteurgaucheDIR2= 6;
  int MoteurgauchePW2 = 3;

String message;
void setup() {
  
  Serial.begin(115200);
  pinMode(MoteurdroiteDIR1, OUTPUT);
  pinMode(MoteurdroitePW1, OUTPUT);
  pinMode(MoteurgaucheDIR2, OUTPUT);
  pinMode(MoteurgauchePW2, OUTPUT);
  do {
    message = Serial.readStringUntil("|");
    if (message == "Hellow Arduino|") {
      Serial.println("ToutEstPret");
    }
  } while (Serial.available() <= 0 || message != "Hellow Arduino|")
;}

void Avancer() {

  analogWrite(MoteurdroiteDIR1, 0);  ///toruner vers l'avant moteur droit
  analogWrite(MoteurdroitePW1, 127);

  analogWrite(MoteurgaucheDIR2, 0);  ///toruner vers l'avant moteur gauche
  analogWrite(MoteurgauchePW2, 127);     
}

void Tourner_a_droite() {

  delay(10000);
  
  analogWrite(MoteurdroiteDIR1, 0);  ///toruner vers l'arrière moteur droit
  analogWrite(MoteurdroitePW1, 150);

  analogWrite(MoteurgaucheDIR2, 0);  ///toruner vers l'arrière moteur droit
  analogWrite(MoteurgauchePW2, 0);
  
}

void Tourner_a_gauche() {

  analogWrite(MoteurdroiteDIR1, 0);  ///toruner vers l'arrière moteur droit
  analogWrite(MoteurdroitePW1, 0);

  analogWrite(MoteurgaucheDIR2, 0);  ///toruner vers l'avant moteur gauche
  analogWrite(MoteurgauchePW2, 127);
}


void decode_message() {
  if (Serial.available() > 0) {
    message = Serial.readStringUntil("|");
    if (message = "Avancer|") {

      Avancer();
    } else if (message = "Tourner_a_droite|") {
      Tourner_a_droite();
    }

    else if (message = "Tourner_a_gauche|") {
      Tourner_a_gauche();
    }
  }
}

void loop() {
     
    decode_message();

}
