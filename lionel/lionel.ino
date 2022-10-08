const int ledPin =  LED_BUILTIN;    // the number of the LED pin
const int x53 = 53;
const int x52 = 52;
const int x51 = 51;
const int x50 = 50;
const int x49 = 49;
const int x48 = 48;
const int x47 = 47;
const int x46 = 46;
const int x45 = 45;
const int x44 = 44;
const int x43 = 43; 
const int x42 = 42;
const int x41 = 41;
const int x40 = 40;
const int x39 = 39;
const int x38 = 38;
const int x37 = 37;
const int x36 = 36;
const int x35 = 35;
const int x34 = 34;
const int x33 = 33;
const int x32 = 32;
const int x31 = 31;
const int x30 = 30;
const int x29 = 29;
const int x28 = 28;
const int x27 = 27;
const int x26 = 26;

// Variables will change:

int ledState = LOW;             // ledState used to set the LED

void setup() {
  // set the digital pins as output:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(x53, OUTPUT);
  pinMode(x52, OUTPUT);
  pinMode(x51, OUTPUT);
  pinMode(x50, OUTPUT);
  pinMode(x49, OUTPUT);
  pinMode(x48, OUTPUT);
  pinMode(x47, OUTPUT);
  pinMode(x46, OUTPUT);
  pinMode(x45, OUTPUT);
  pinMode(x44, OUTPUT);
  pinMode(x43, OUTPUT);
  pinMode(x42, OUTPUT);
  pinMode(x41, OUTPUT);
  pinMode(x40, OUTPUT);
  pinMode(x39, OUTPUT);
  pinMode(x38, OUTPUT);
  pinMode(x37, OUTPUT);
  pinMode(x36, OUTPUT);
  pinMode(x35, OUTPUT);
  pinMode(x34, OUTPUT);
  pinMode(x33, OUTPUT);
  pinMode(x32, OUTPUT);
  pinMode(x31, OUTPUT);
  pinMode(x30, OUTPUT);
  pinMode(x29, OUTPUT);
  pinMode(x28, OUTPUT);
  pinMode(x27, OUTPUT);
  pinMode(x26, OUTPUT);
}


String incomingByte;  

void loop() {

// Check for incoming serial bytes

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

// BLOCK POWER

// Main Line 1  (BLACK)
    if (incomingByte == "m1ON") {
      digitalWrite(x34, HIGH);   
    }
    else if (incomingByte == "m1OFF") {
      digitalWrite(x34, LOW);      
    }

// Main Line 2  (BLACK)
    if (incomingByte == "m2ON") {
      digitalWrite(x35, HIGH); 
    }
    else if (incomingByte == "m2OFF") {
      digitalWrite(x35, LOW);
    }

// Main Line 3 (BLACK)
    if (incomingByte == "m3ON") {
      digitalWrite(x36, HIGH);
    }
    else if (incomingByte == "m3OFF") {
      digitalWrite(x36, LOW);
    }
    
// City Line 1 (BLUE)
    if (incomingByte == "s1ON") {
      digitalWrite(x37, HIGH);
    }
    else if (incomingByte == "s1OFF") {
      digitalWrite(x37, LOW);
    }

// City Line 2 (BLUE)
    if (incomingByte == "s2ON") {
      digitalWrite(x38, HIGH);
    }
    else if (incomingByte == "s2OFF") {
      digitalWrite(x38, LOW);
    }
    
// City Line 3 (BLUE)
    if (incomingByte == "s3ON") {
      digitalWrite(x39, HIGH);   
    }
    else if (incomingByte == "s3OFF") {
      digitalWrite(x39, LOW); 
    }

// Station 1 (BLUE)
    if (incomingByte == "s4ON") {
      digitalWrite(x40, HIGH);
    }
    else if (incomingByte == "s4OFF") {
      digitalWrite(x40, LOW);
  
    }

// Station 2 (BLUE)
    if (incomingByte == "s5ON") {
      digitalWrite(x41, HIGH);
    }
    else if (incomingByte == "s5OFF") {
      digitalWrite(x41, LOW);
    }



// Engine Barn 1 (BLUE)
//    if (incomingByte == "s6ON") {
//      digitalWrite(SPDT_, LOW);
//    }
//    else if (incomingByte == "s6OFF") {
//      digitalWrite(SPDT_, HIGH);
//    }

// Engine Barn 2 (BLUE)
//    if (incomingByte == "s7ON") {
//      digitalWrite(SPDT_, LOW);
//    }
//    else if (incomingByte == "s7OFF") {
//      digitalWrite(SPDT_, HIGH); 
//    }



// SWITCHES
   
    if (incomingByte == "Switch1ON") {
      digitalWrite(x53, HIGH);
      digitalWrite(x51, HIGH);
    }
    else if (incomingByte == "Switch1OFF") {
      digitalWrite(x53, LOW);
      digitalWrite(x51, LOW);
    }
 
    if (incomingByte == "Switch2ON") {
      digitalWrite(x52, HIGH);
      digitalWrite(x50, HIGH);
    }
    else if (incomingByte == "Switch2OFF") {
      digitalWrite(x52, LOW);
      digitalWrite(x50, LOW);  
    }
    
    if (incomingByte == "Switch3ON") {
      digitalWrite(x49, HIGH);
    }
    else if (incomingByte == "Switch3OFF") {
      digitalWrite(x49, LOW);
    }
   
    if (incomingByte == "Switch4ON") {
      digitalWrite(x48, HIGH);
    }
    else if (incomingByte == "Switch4OFF") {
      digitalWrite(x48, LOW); 
    }
    
    if (incomingByte == "Switch5ON") {
      digitalWrite(x47, HIGH);
    }
    else if (incomingByte == "Switch5OFF") {
      digitalWrite(x47, LOW);
    }
    
    if (incomingByte == "Switch6ON") {
      digitalWrite(x46, HIGH);
    }
    else if (incomingByte == "Switch6OFF") {
      digitalWrite(x46, LOW);
    }

    if (incomingByte == "Switch7ON") {
      digitalWrite(x45, HIGH);
    }
    else if (incomingByte == "Switch7OFF") {
      digitalWrite(x45, LOW);
    }

    if (incomingByte == "Switch8ON") {
      digitalWrite(x44, HIGH);
    }
    else if (incomingByte == "Switch8OFF") {
      digitalWrite(x44, LOW);
    }
    if (incomingByte == "Switch9ON") {
      digitalWrite(x43, HIGH);
    }
    else if (incomingByte == "Switch9OFF") {
      digitalWrite(x43, LOW);
    }
    if (incomingByte == "Switch10ON") {
      digitalWrite(x42, HIGH);
    }
    else if (incomingByte == "Switch10OFF") {
      digitalWrite(x42, LOW);
    }


// DC-4.5 Volt Accessories
   
    if (incomingByte == "acc1ON") {
      digitalWrite(x33, HIGH);
    }
    else if (incomingByte == "acc1OFF") {
      digitalWrite(x33, LOW);

    if (incomingByte == "acc2ON") {
      digitalWrite(x32, HIGH);
    }
    else if (incomingByte == "acc2OFF") {
      digitalWrite(x32, LOW);
    }  
    if (incomingByte == "acc3ON") {
      digitalWrite(x31, HIGH);
    }
    else if (incomingByte == "acc3OFF") {
      digitalWrite(x31, LOW);
    }
    if (incomingByte == "acc4ON") {
      digitalWrite(x30, HIGH);
    }
    else if (incomingByte == "acc4OFF") {
      digitalWrite(x30, LOW);
    }
    

//AC-18 Volt Accessories
    if (incomingByte == "acc5ON") {
      digitalWrite(x29, HIGH);
    }
    else if (incomingByte == "acc5OFF") {
      digitalWrite(x29, LOW);
    }
    if (incomingByte == "acc6ON") {
      digitalWrite(x28, HIGH);
    }
    else if (incomingByte == "acc6OFF") {
      digitalWrite(x28, LOW);
    }
    if (incomingByte == "acc7ON") {
      digitalWrite(x27, HIGH);
    }
    else if (incomingByte == "acc7OFF") {
      digitalWrite(x27, LOW);
    }
    if (incomingByte == "acc8ON") {
      digitalWrite(x26, HIGH);
    }
    else if (incomingByte == "acc8OFF") {
      digitalWrite(x26, LOW);
    }
  }
   
  }  
}

  
