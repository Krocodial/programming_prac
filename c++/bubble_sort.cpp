#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	for(int i=0; i<argc; i++)
		cout << argv[i] << endl;
ifstream myfile;
myfile.open(argv[1], ios::in);

string line;
if(myfile.is_open()){
	while(getline(myfile,line))
		cout << line << '\n';
	myfile.close();
}
else{
	cout << "unable to open file \n";
}
return 0;



}
