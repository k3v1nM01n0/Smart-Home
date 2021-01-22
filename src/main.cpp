#include <Arduino.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <ESP8266WiFi.h>

#define SSID "SSID"
#define PASS "PASS"




//GPIO pins
const int LED1 = 5;
const int LED2 = 0;
const int LED3 = 2;

WiFiServer server(8081);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println();
  Serial.println();



  //Initialize output variables
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  Serial.println();
  Serial.println();

  //Connecting to wifi
  Serial.printf("Connecting to:");
  Serial.println(SSID);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASS);

  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.printf(".");
  }
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
  Serial.printf("server started");

}

void loop() {
  // put your main code here, to run repeatedly:
  
  WiFiClient client = server.available();
  
  if (!client){
    return ;
  }
  while(!client.available()){
    Serial.printf("Client not available\r\n");
    delay(100);
  }
  Serial.printf("Connecting to client\r\n");
  
  //Receive client data 
  char buffer[3];
  int id, state;
  int count = 0;
  while (client.available()){
    Serial.printf("receiving data from client\r\n");
    count += client.read((uint8_t*)buffer+count, 3);

    //validate data
    if(count == 3){
        break;
    }
  }
  
    id = buffer[0];
    state = buffer[2];

    Serial.printf("id:%d  state:%d\r\n", id - '0', state -'0');

    if(state != '1' && state != '0'){
       client.write("ERROR");
       client.stop();
       return;
    }

    // turn GPIO on and off
    if(id == '1'){
        if(state == '1'){
            digitalWrite(LED1, HIGH);
        }else if(state == '0'){
            digitalWrite(LED1, LOW);
        }
    }else if(id == '2'){
        if(state == '1'){
            digitalWrite(LED2, HIGH);
        }else if(state == '0'){
            digitalWrite(LED2, LOW);
        }
    }else if(id == '3'){
        if(state == '1'){
            digitalWrite(LED3, HIGH);
        }else if(state == '0'){
            digitalWrite(LED3, LOW);
        }
    }else{
      client.write("ERROR");
    }

  client.write("OK");
    
  Serial.println();
  client.stop();


}
