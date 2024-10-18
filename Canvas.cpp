#include "Canvas.h"

Canvas::~Canvas() {
    clear();
}

void Canvas::addShape(Shape* shape) {
    shapes.push_back(shape);
}

void Canvas::clear() {
    for (auto shape : shapes) {
        delete shape;
    }
    shapes.clear();
}

void Canvas::show(sf::RenderWindow& window) {
    for (const auto& shape : shapes) {
        shape->draw(window);
    }
}
