#include <math.h>
#include <SoftwareSerial.h>
#include <dht.h>
#define DHT11_PIN 7
#define samp_siz 4
#define rise_threshold 5
SoftwareSerial BTserial(10, 11); // RX | TX
SoftwareSerial mySerial(10, 11); 
String isim = "Arduino UNO";
int sifre = 1234;
int sensorPin = 0;
String uart = "9600,0,0";
void setup() {
  BTserial.begin(9600); 
  Serial.begin(9600); 
Serial.println("HC-05 Modul Ayarlaniyor…"); 
Serial.println("Lutfen 5 sn icinde HC-05 modulun uzerindeki butona basili tutarak baglanti yapiniz."); 
mySerial.begin(38400); 
delay(5000); 
mySerial.print("AT+NAME="); 
mySerial.println(isim); 
Serial.print("Isim ayarlandi: "); 
Serial.println(isim); 
delay(1000); 
mySerial.print("AT+PSWD="); 
mySerial.println(sifre); 
Serial.print("Sifre ayarlandi: "); 
Serial.println(sifre); 
delay(1000); 
mySerial.print("AT+UART="); 
mySerial.println(uart); 
Serial.print("Baud rate ayarlandi: "); 
Serial.println(uart); 
delay(2000); 
Serial.println("Islem tamamlandi.");}
void loop ()
{
   float reads[samp_siz], sum;
   long int now, ptr;
   float last, reader, start;
   float first, second, third, before, print_value;
   bool rising;
   int rise_count;
   int n;
   long int last_beat;
   for (int i = 0; i < samp_siz; i++)
     reads[i] = 0;
   sum = 0;
   ptr = 0;
   while(1)
   {
     // calculate an average of the sensor
     // during a 20 ms period (this will eliminate
     // the 50 Hz noise caused by electric light
     n = 0;
     start = millis();
     reader = 0.;
     do
     {
       reader += analogRead (sensorPin);
       n++;
       now = millis();
     }
     while (now < start + 20);  
     reader /= n;  // we got an average
     // Add the newest measurement to an array
     // and subtract the oldest measurement from the array
     // to maintain a sum of last measurements
     sum -= reads[ptr];
     sum += reader;
     reads[ptr] = reader;
     last = sum / samp_siz;
     // now last holds the average of the values in the array
     // check for a rising curve (= a heart beat)
     if (last > before)
     {
       rise_count++;
       if (!rising && rise_count > rise_threshold)
       {
         // Ok, we have detected a rising curve, which implies a heartbeat.
         // Record the time since last beat, keep track of the two previous
         // times (first, second, third) to get a weighed average.
         // The rising flag prevents us from detecting the same rise 
         // more than once.
         rising = true;
         first = millis() - last_beat;
         last_beat = millis();
         // Calculate the weighed average of heartbeat rate
         // according to the three last beats
         print_value = 60000. / (0.4 * first + 0.3 * second + 0.3 * third);
         Serial.print(print_value);
         Serial.print('\n');
         third = second;
         second = first;
           dht DHT;
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(1000);
BTserial.print("1234");

BTserial.print(",");

BTserial.print(print_value);

BTserial.print(",");

BTserial.print(DHT.temperature);

BTserial.print(",");

BTserial.print(DHT.humidity);

BTserial.print(";");

//message to the receiving device

delay(20);
}
     }
     else
     {
       // Ok, the curve is falling
       rising = false;
       rise_count = 0;
     }
     before = last;
     ptr++;
     ptr %= samp_siz;
   }
}
