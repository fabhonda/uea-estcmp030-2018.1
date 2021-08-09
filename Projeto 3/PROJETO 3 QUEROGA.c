#include<stdio.h>
#include<stdlib.h>

char fita1[200], fita2[200], fita3[200], fita4[200], operacao[50], sinal;
int i = 100, j=100, k = 100, x = 100, tam = 0, resultado = 0;

void q1();
void q2();
void q3();
void q4();
void qaceita();

int main(){
	int y;
	for(y = 0; y<200;y++){
		fita1[y] = '_';
		fita2[y] = '_';
		fita3[y] = '_';
		fita4[y] = '_';
	}
	scanf("%s",operacao);
	y = 0;
	while(operacao[y] != '\0'){
		fita1[i] = operacao[y];
		i++;
		y++;
	}
	q1();
	
	if(resultado == 0){
		printf("%s REJEITA",operacao);
	}	
return 0;	
}


void q1(){
	i = 100;
	while(fita1[i]=='0' || fita1[i]=='1'){
		fita2[j] = fita1[j];
		i++;
		j++;
	}
	sinal = fita1[i];
	if(sinal=='+' || sinal=='-'){
		q2();
	}
}

void q2(){
	i++;
	if(fita1[i]=='0' || fita1[i]=='1'){
		while(fita1[i] != '_'){
			fita3[k] = fita1[i];
			i++;
			k++;
		}
		if(sinal == '+'){
			q3();
		}else if(sinal == '-'){
			q4();
		}
	}
}

void q3(){
	j--;
	k--;
	int sobe = 0;
	while(fita2[j]!='_'){
		if(fita2[j]=='0' && fita3[k]=='0' && sobe==0){
			fita4[x] = '0';
		}else if(fita2[j]=='0' && fita3[k]=='1' && sobe==0){
			fita4[x] = '1';
		}else if(fita2[j]=='1' && fita3[k]=='0' && sobe==0){
			fita4[x] = '1';
		}else if(fita2[j]=='1' && fita3[k]=='1' && sobe==0){
			fita4[x] = '0';
			sobe = 1;
		}else if(fita2[j]=='0' && fita3[k]=='0' && sobe==1){
			fita4[x] = '1';
			sobe = 0;
		}else if(fita2[j]=='0' && fita3[k]=='1' && sobe==1){
			fita4[x] = '0';
		}else if(fita2[j]=='1' && fita3[k]=='0' && sobe==1){
			fita4[x] = '0';
		}else if(fita2[j]=='1' && fita3[k]=='1' && sobe==1){
			fita4[x] = '1';
		}else if(fita2[j]=='1' && fita3[k]=='_' && sobe==1){
			fita4[x] = '0';
		}else if(fita2[j]=='0' && fita3[k]=='_' && sobe==1){
			fita4[x] = '1';
			sobe = 0;
		}else if(fita2[j]=='1' && fita3[k]=='_' && sobe==0){
			fita4[x] = '1';
		}else if(fita2[j]=='0' && fita3[k]=='_' && sobe==0){
			fita4[x] = '0';
		}
		
		j--;
		k--;
		x--;
		tam++;
	}
	if (fita3[k] != '_'){
		while(fita3[k]!='_'){
			if(fita2[j]=='_' && fita3[k]=='1' && sobe==1){
			fita4[x] = '0';
			}else if(fita2[j]=='_' && fita3[k]=='0' && sobe==1){
			fita4[x] = '1';
			sobe = 0;
			}else if(fita2[j]=='_' && fita3[k]=='1' && sobe==0){
			fita4[x] = '1';
			}else if(fita2[j]=='_' && fita3[k]=='0' && sobe==0){
			fita4[x] = '0';
			}
			
			k--;
			x--;
			tam++;
		}
	}
	
	
	if(sobe == 1){
		fita4[x] = '1';
		tam++;
		x--;
	}
	
	char resp[tam];
	tam=0;
	x++;
	while(fita4[x] != '_'){
		resp[tam] = fita4[x];
		x++;
		tam++;
	}
	resp[tam] = '\0';
	qaceita(resp);
}

void q4(){
	j--;
	k--;
	int empresta = 0;
	while(fita2[j]!='_' && fita2[j]!='_'){
		if(fita2[j]=='0' && fita3[k]=='0' && empresta==0){
			fita4[x] = '0';
		}else if(fita2[j]=='0' && fita3[k]=='1' && empresta==0){
			fita4[x] = '1';
			empresta = 1;
		}else if(fita2[j]=='1' && fita3[k]=='0' && empresta==0){
			fita4[x] = '1';
		}else if(fita2[j]=='1' && fita3[k]=='1' && empresta==0){
			fita4[x] = '0';
		}else if(fita2[j]=='0' && fita3[k]=='0' && empresta==1){
			fita4[x] = '1';
			empresta = 1;
		}else if(fita2[j]=='1' && fita3[k]=='0' && empresta==1){
			fita4[x] = '0';
			empresta = 0;
		}else if(fita2[j]=='1' && fita3[k]=='1' && empresta==1){
			fita4[x] = '0';
			empresta = 1;
		}else if(fita2[j]=='0' && fita3[k]=='1' && empresta==1){
			fita4[x] = '0';
			empresta = 1;
		}
		j--;
		k--;
		x--;
		tam++;
	}
	
	char resp[tam];
	tam=0;
	x++;
	while(fita4[x] != '_'){
		resp[tam] = fita4[x];
		x++;
		tam++;
	}
	resp[tam] = '\0';
	qaceita(resp);
}


void qaceita(char resp[]){
	resultado = 1;
	printf("%s=%s ACEITA",operacao,resp);
}

