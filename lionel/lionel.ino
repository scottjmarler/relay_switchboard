const int ledPin =  LED_BUILTIN;    
const int x25 = 30;
const int x24 = 29;
const int x23 = 28;
const int x22 = 27;
const int x21 = 26;

int ledState = LOW;             

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(x25, OUTPUT);
  pinMode(x24, OUTPUT);
  pinMode(x23, OUTPUT);
  pinMode(x22, OUTPUT);
  pinMode(x21, OUTPUT);
}

String incomingByte;  

void loop() {

  if (Serial.available() > 0) {
  incomingByte = Serial.readStringUntil('\n');

// INTERNAL LED 

    if (incomingByte == "on") {
      digitalWrite(ledPin, HIGH);
      Serial.write("Led on");
    }
    else if (incomingByte == "off") {
      digitalWrite(ledPin, LOW);
    }

// Building Lights
    if (incomingByte == "buildings_ON") {
      digitalWrite(x21, HIGH);   
    }
    else if (incomingByte == "buildings_OFF") {
      digitalWrite(x21, LOW);      
    }

// Street Lights
    if (incomingByte == "street_ON") {
      digitalWrite(x22, HIGH); 
    }
    else if (incomingByte == "street_OFF") {
      digitalWrite(x22, LOW);
    }

// Operating Accessories
    if (incomingByte == "acc_ON") {
      digitalWrite(x23, HIGH);
    }
    else if (incomingByte == "acc_OFF") {
      digitalWrite(x23, LOW);
    }

// Signal Lights

   if (incomingByte == "acc_ON") {
     digitalWrite(x24, HIGH);
   }
   else if (incomingByte == "acc_OFF") {
     digitalWrite(x24, LOW);
   }
    
}
}

  
