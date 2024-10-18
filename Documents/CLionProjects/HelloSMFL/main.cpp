#include "Canvas.h"
#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>

using namespace std;

sf::Color getColorFromString(string &color) {
    if (color == "red") {
        return sf::Color::Red;
    }
    if (color == "green") {
        return sf::Color::Green;
    }
    if (color == "blue") {
        return sf::Color::Blue;
    }
    if (color == "yellow") {
        return sf::Color::Yellow;
    }
    return sf::Color::White;
}

int main() {
    sf::RenderWindow window (sf::VideoMode(800,600), "Graphis");
    Canvas canvas;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        string shapeType;
        cout << "Введите тип фигуры (Point, Line, Ellipse, Rectangle, Polygon) или 'exit' для выхода:";
        cin >> shapeType;
        if (shapeType == "exit") {
            break;
        }

        string colorStr;
        cout << "color? (red, green, blue, yellow): ";
        cin >> colorStr;
        sf::Color color = getColorFromString(colorStr);

        if (shapeType == "point") {
            int x,y;
            cout << "enter coords x and y: " << endl;
            cin >> x >> y;
            canvas.addShape(new Point(x,y, color));

        }
        else if (shapeType == "line") {
            int x1,x2,y1,y2;
            cout << "enter coords x1, y1, x2, y2: ";
            cin >> x1 >> y1 >> x2 >> y2;
            canvas.addShape(new Line(Point(x1,y1,color), Point(x2,y2,color), color));
        }
        else if (shapeType == "ellipse") {
            int x1,y1,x2,y2;
            bool filled;
            cout << "enter coords x1, y1, x2, y2 and fill(0 or 1)" << endl;
            cin >> x1 >> y1 >> x2 >> y2 >> filled;
            canvas.addShape(new Ellipse(x1,y1,x2,y2, color, filled));
        }
        else if (shapeType == "rectangle") {
            int x1,y1,x2,y2;
            bool filled;
            cout << "enter coords x1, y1, x2, y2 and fill(0 or 1): " << endl;
            cin >> x1 >> y1 >> x2 >> y2 >> filled;
            canvas.addShape(new Rectangle(x1,y1,x2,y2, color, filled));
        }
        else if (shapeType == "polygon") {
            int n;
            cout <<  "enter number of vertices: ";
            cin >> n;
            vector <Point> vertices;
            for (int i = 0; i < n; i++) {
                int x,y;
                cout << "enter coords of vertices number: " <<  i+1 << endl;
                cin >> x >> y;
                vertices.emplace_back(x,y,color);
            }

            bool filled;
            cout << "enter fill (0 or 1)" << endl;
            cin >> filled;
            canvas.addShape(new Polygon(vertices, color, filled));
        }

            window.clear();
            canvas.show(window);
            window.display();

    }


return 0;
}