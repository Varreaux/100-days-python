#include<iostream>
#include<string>
#include<fstream>

using namespace std;

string change (string title);

int main (){

    string str = "17menu_resources";
    string answer = change(str);
    //string realAnswer = "dailyStreak/" + answer; 
    string realAnswer = "practice/" + answer; 
    

    ofstream outFile;
    outFile.open(answer);
    cout<<answer<<endl<<endl;
    
    // outFile<<"#include<iostream>"<<endl;

}

string change (string title){
    title.insert(2,1,'_');
    for(int i = 1; i < title.length()-1; i++){
        if(title[i] == ' ') title[i]='_';
    }
    return "Day"+title+".py";
}