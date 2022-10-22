#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class A
{
public:
    int a;
    A()
    {
        a = 10;
        cout << "a: " << a << endl;
    }
};
class B : virtual public A
{
public:
    int b;
    B()
    {
        b = 20;
        a = 12;
        cout << "b: " << b << " a: " << a << endl;
    }
};
class C : virtual public A
{
public:
    int c;
    C()
    {
        c = 30;
        cout << "c: " << c << " a: " << a << endl;
    }
};
class D : public B, public C
{
public:
    int d;
    D()
    {
        d = 40;
        cout << "d: " << d << endl;
    }
    void get_value()
    {
        cout << "a : " << a << " b : " << b <<" c : " << c << " d : " << d << endl;
    }
};

int main()
{
    D obj;
    obj.get_value();
    return 0;
}