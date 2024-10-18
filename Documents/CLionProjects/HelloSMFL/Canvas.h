#ifndef CANVAS_H
#define CANVAS_H

#include <SFML/Graphics.hpp>
#include <vector>
#include <string>
#include <iostream>


class Shape {
public:
    virtual void draw(sf::RenderWindow& window) const = 0;
    virtual ~Shape() = default;
};

// Класс для точки
class Point : public Shape {
public:
    int x, y;
    sf::Color color;

    Point(int x, int y, sf::Color color) : x(x), y(y), color(color) {}

    void draw(sf::RenderWindow& window) const override {
        sf::CircleShape point(2);
        point.setFillColor(color);
        point.setPosition(x, y);
        window.draw(point);
    }
};


class Line : public Shape {
public:
    Point start, end;
    sf::Color color;

    Line(Point start, Point end, sf::Color color)
        : start(start), end(end), color(color) {}

    void draw(sf::RenderWindow& window) const override {
        sf::Vertex line[] = {
            sf::Vertex(sf::Vector2f(start.x, start.y), color),
            sf::Vertex(sf::Vector2f(end.x, end.y), color)
        };
        window.draw(line, 2, sf::Lines);
    }
};


class Ellipse : public Shape {
public:
    int x1, y1, x2, y2;
    sf::Color color;
    bool filled;

    Ellipse(int x1, int y1, int x2, int y2, sf::Color color, bool filled)
        : x1(x1), y1(y1), x2(x2), y2(y2), color(color), filled(filled) {}

    void draw(sf::RenderWindow& window) const override {
        sf::CircleShape ellipse((x2 - x1) / 2);
        ellipse.setPosition(x1, y1);
        ellipse.setFillColor(filled ? color : sf::Color::Transparent);
        ellipse.setOutlineColor(color);
        ellipse.setOutlineThickness(5);
        window.draw(ellipse);
    }
};


class Rectangle : public Shape {
public:
    int x1, y1, x2, y2;
    sf::Color color;
    bool filled;

    Rectangle(int x1, int y1, int x2, int y2, sf::Color color, bool filled)
        : x1(x1), y1(y1), x2(x2), y2(y2), color(color), filled(filled) {}

    void draw(sf::RenderWindow& window) const override {
        sf::RectangleShape rectangle(sf::Vector2f(x2 - x1, y2 - y1));
        rectangle.setPosition(x1, y1);
        rectangle.setFillColor(filled ? color : sf::Color::Transparent);
        rectangle.setOutlineColor(color);
        rectangle.setOutlineThickness(1);
        window.draw(rectangle);
    }
};


class Polygon : public Shape {
public:
    std::vector<Point> vertices;
    sf::Color color;
    bool filled;

    Polygon(std::vector<Point> vertices, sf::Color color, bool filled)
        : vertices(vertices), color(color), filled(filled) {}

    void draw(sf::RenderWindow& window) const override {
        sf::ConvexShape polygon;
        polygon.setPointCount(vertices.size());
        for (size_t i = 0; i < vertices.size(); ++i) {
            polygon.setPoint(i, sf::Vector2f(vertices[i].x, vertices[i].y));
        }
        polygon.setFillColor(filled ? color : sf::Color::Transparent);
        polygon.setOutlineColor(color);
        polygon.setOutlineThickness(1);
        window.draw(polygon);
    }
};


class Canvas {
private:
    std::vector<Shape*> shapes;
public:
    ~Canvas();
    void addShape(Shape* shape);
    void clear();
    void show(sf::RenderWindow& window);
};

#endif // CANVAS_H
