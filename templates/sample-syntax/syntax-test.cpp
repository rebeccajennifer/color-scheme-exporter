// =============================================
//   C++ Highlighting Showcase for VS Code
//   (Extended: Regex, Lambdas, Constexpr, Operators)
// =============================================

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <regex>
#include <map>
#include <memory>
#include <algorithm>

// ----- Macros -----
#define PI 3.14159265358979323846
#define SQUARE(x) ((x) * (x))

using a = double;

// ----- Namespaces -----
namespace math_utils {
  inline double circle_area(double radius) {
    return PI * SQUARE(radius);
  }

  constexpr double circle_circumference(double radius) {
    return 2 * PI * radius;
  }
}

// ----- Enums -----
enum class Color { Red, Green, Blue };
enum class ShapeType : int { Circle, Square, Triangle };

// ----- Structs and Classes -----
struct Point {
  double x;
  double y;
};

class Shape {
protected:
  std::string name;
public:
  explicit Shape(std::string n) : name(std::move(n)) {}
  virtual double area() const = 0;
  virtual ~Shape() = default;

  virtual void describe() const {
    std::cout << "Shape: " << name << std::endl;
  }
};

// ----- Derived Class with Templates and Static Member -----
template <typename T>
class Circle : public Shape {
  T radius;
  static inline int instanceCount = 0;

public:
  explicit Circle(T r) : Shape("Circle"), radius(r) { ++instanceCount; }
  ~Circle() override { --instanceCount; }

  static int getInstanceCount() { return instanceCount; }

  double area() const override {
    return math_utils::circle_area(static_cast<double>(radius));
  }

  void scale(double factor) { radius *= factor; }

  T getRadius() const { return radius; }

  // Overloaded operator
  bool operator<(const Circle& other) const { return radius < other.radius; }
};

// ----- Free Functions, Regex, and Lambdas -----
inline double distance(const Point& a, const Point& b) {
  double dx = a.x - b.x;
  double dy = a.y - b.y;
  return std::sqrt(dx * dx + dy * dy);
}

void demonstrateRegex() {
  std::string text = "Emails: alice@example.com, bob.smith@domain.org";
  std::regex pattern(R"(([\w\.-]+)@([\w\.-]+\.\w+))");

  std::smatch matches;
  std::cout << "Regex matches in: " << text << "\n";
  auto wordsBegin = std::sregex_iterator(text.begin(), text.end(), pattern);
  auto wordsEnd = std::sregex_iterator();

  for (auto it = wordsBegin; it != wordsEnd; ++it) {
    std::smatch m = *it;
    std::cout << "Full match: " << m.str(0)
              << " | user: " << m.str(1)
              << " | domain: " << m.str(2) << "\n";
  }

  // Replace example
  std::string masked = std::regex_replace(text, pattern, "hidden@domain");
  std::cout << "Masked: " << masked << "\n";
}

// ----- Demonstration Function -----
void demonstrate() {
  // Constants and Containers
  const int count = 3;
  std::vector<double> values = {1.0, 2.0, 3.0};

  // Lambda with capture
  double scale_factor = 2.0;
  auto scaleValue = [scale_factor](double v) { return v * scale_factor; };

  Circle<float> c(5.0f);
  Shape* s = &c;

  s->describe();
  std::cout << "Area: " << s->area() << std::endl;

  // Use regex demo
  demonstrateRegex();

  // Control Flow
  for (int i = 0; i < count; ++i) {
    if (values[i] > 2.0) {
      std::cout << "Value " << i << " is large.\n";
    } else {
      std::cout << "Value " << i << " is small.\n";
    }
  }

  // Enums and Switch
  ShapeType type = ShapeType::Circle;
  switch (type) {
    case ShapeType::Circle:
      std::cout << "Shape is Circle.\n";
      break;
    case ShapeType::Square:
      std::cout << "Shape is Square.\n";
      break;
    default:
      std::cout << "Shape is Other.\n";
  }

  // Pointers, smart pointers, and regex replacement in maps
  Point p1{0, 0}, p2{3, 4};
  auto dist = std::make_unique<double>(distance(p1, p2));
  std::cout << "Distance: " << *dist << std::endl;

  std::map<std::string, Circle<double>> shapeMap = {
    {"small", Circle<double>(2.0)},
    {"large", Circle<double>(10.0)}
  };

  for (auto& [key, shape] : shapeMap) {
    std::cout << key << ": area=" << shape.area() << "\n";
  }

  // Regex-based filtering in map keys
  std::regex smallPattern("small");
  for (auto& [key, shape] : shapeMap) {
    if (std::regex_search(key, smallPattern))
      std::cout << "Matched key: " << key << "\n";
  }

  std::cout << "Active Circles: " << Circle<double>::getInstanceCount() << "\n";
}

// ----- Entry Point -----
int main() {
  demonstrate();
  return 0;
}
