class ThreadDemo implements Runnable {
    ThreadDemo() {
        Thread ct = Thread.currentThread(); // Основной поток хранится в переменной ct
        Thread t = new Thread(this, "Demo Thread"); // Создаётся поток в t
        t.start(); // Запускает поток t
        try {
            Thread.sleep(3000); // Созданный поток переведем в режим ожидания на 1 секунды
        } catch (InterruptedException e) {
        }
    }
    public void run() {
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("" + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
        }
    }
    public static void main(String args[]) {
        new ThreadDemo();
    }
}