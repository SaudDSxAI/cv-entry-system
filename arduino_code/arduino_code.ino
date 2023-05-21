int trig1=2,echo1=3,trig2=4,echo2=5;
double distance1, duration1,distance2, duration2;
int pin1=6,pin2 =9,pin3=10,pin4=8;
int counter =0;
void setup() 
{
  Serial.begin(9600);
  pinMode(trig1,OUTPUT);
  pinMode(trig2,OUTPUT);
  pinMode(echo1,INPUT);
  pinMode(echo2,INPUT);
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,INPUT);
  
}


void loop() 
{
  
    analogWrite(pin1,LOW);
    analogWrite(pin2,LOW);
    analogWrite(pin3,LOW);
    
    
   
   

  // distance1
    //*******************************
    digitalWrite(trig1, LOW);
    delayMicroseconds(2);

    digitalWrite(trig1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig1, LOW);

    duration1 = pulseIn(echo1, HIGH);
    distance1 = (duration1 * 0.034) / 2;
    //*******************************

    // distance2
    //*******************************
    digitalWrite(trig2, LOW);
    delayMicroseconds(2);

    digitalWrite(trig2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig2, LOW);

    duration2 = pulseIn(echo2, HIGH);
    distance2 = (duration2 * 0.034) / 2;
    //******************************



    if(distance1 < 20)
    {
      Serial.println("Entry");
      analogWrite(pin1,150);
      delay(1000);
    }
    while(distance1 < 50)
    {
      // distance1
    //*******************************
    digitalWrite(trig1, LOW);
    delayMicroseconds(2);

    digitalWrite(trig1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig1, LOW);

    duration1 = pulseIn(echo1, HIGH);
    distance1 = (duration1 * 0.034) / 2;
    //*******************************
    }
  
    

    if(distance2 <20)
    {
      Serial.println("Exit");
      analogWrite(pin2,150);
      delay(1000);
    }
    
    while(distance2 <50)
    {
      // distance2
    //*******************************
    digitalWrite(trig2, LOW);
    delayMicroseconds(2);

    digitalWrite(trig2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig2, LOW);

    duration2 = pulseIn(echo2, HIGH);
    distance2 = (duration2 * 0.034) / 2;
    //******************************
    }


if(!digitalRead(pin4))
{

      Serial.println("Terminate");
      analogWrite(pin3,150);
      delay(1000);
  
}

    
   

}
