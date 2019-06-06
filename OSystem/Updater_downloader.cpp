//
// Created by i on 29.05.19.
//

#ifndef VSUCODING_UPDATER_DOWNLOADER_H
#define VSUCODING_UPDATER_DOWNLOADER_H

#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

void Work(int &a) {
    cout << "Start second thread " << this_thread::get_id() << endl;
    this_thread::sleep_for(chrono::milliseconds(5000));
    a *= 2;
    this_thread::sleep_for(chrono::milliseconds(5000));
    cout << "End second thread " << this_thread::get_id();
}

int Work_ret(int a,int b) {
    cout << "Start third thread " << this_thread::get_id() << endl;
    this_thread::sleep_for(chrono::milliseconds(5000));
    b = b + a;
    this_thread::sleep_for(chrono::milliseconds(5000));
    cout << "End third thread " << this_thread::get_id();
    return b;
}

int main() {
    int a = 2;
    int b = 5;
    int result;
    thread th(Work, std::ref(a));
    thread thb([&result]() { result = Work_ret(2, 5); });
    for (int i = 0; i < 10; i++) {
        cout << "Main thread " << this_thread::get_id() << endl;
        this_thread::sleep_for(chrono::milliseconds(2000));
    }
    th.join();
    thb.join();
    cout << "End main thread " << this_thread::get_id() << endl;

    return 0;
}


#endif //VSUCODING_UPDATER_DOWNLOADER_H
