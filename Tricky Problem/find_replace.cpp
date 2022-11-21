#include <algorithm>
#include <iostream>
#include <string>
using namespace std;


string findAndReplace (string str, string from, string to )
{
   int pos = 0;
   int flen = from.length();
   int tlen = to.length();
   while ((pos = str.find(from, pos))!= -1)
   {
       str.replace(pos, flen, to );
       pos += tlen;
   }
   return str;
}


int main() {
  string line, sstr, rstr, temp;
  cout << "Single Line Input String: " << endl;
  getline(cin, line);
  cout << "Search String: " << endl;
  getline(cin, sstr);
  cout << "Replace String: " << endl;
  getline(cin, rstr);
  temp = ' ';
  sstr = sstr + temp;
  rstr = rstr + temp;
  // ToDo
  
  cout<<findAndReplace(line,sstr,rstr);;
  return 0;
}