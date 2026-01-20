// =============================================
//   JavaScript Highlighting Showcase for VS Code
// =============================================

// ----- Imports and Exports -----
import fs from "fs";
import path from "path";
export const VERSION = "1.0.0";
export default function main() {
  console.log("Highlighting Showcase");
}

// ----- Constants, Variables, and Literals -----
const PI = 3.14159;
let count = 0;
var debugMode = true;
const colors = ["red", "green", "blue"];
const settings = { theme: "flux-pastel", version: VERSION };

// ----- Enums (simulated) -----
const ShapeType = Object.freeze({
  Circle: "circle",
  Square: "square",
  Triangle: "triangle"
});

// ----- Functions, Arrows, Async/Await -----
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;

async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error ${response.status}`);
    const data = await response.json();
    return data;
  } catch (err) {
    console.error("Fetch failed:", err);
    return null;
  }
}

// ----- Classes, Inheritance, Static, Getters/Setters -----
class Shape {
  constructor(name) {
    this.name = name;
  }

  area() {
    throw new Error("Method not implemented");
  }

  static describe() {
    return "A geometric shape";
  }
}

class Circle extends Shape {
  #radius;

  constructor(radius) {
    super("Circle");
    this.#radius = radius;
  }

  get radius() {
    return this.#radius;
  }

  set radius(value) {
    if (value < 0) throw new RangeError("Radius must be positive");
    this.#radius = value;
  }

  area() {
    return PI * this.#radius ** 2;
  }
}

// ----- Destructuring, Spread, Rest -----
function summarize({ name, area }, ...others) {
  return { name, area, count: others.length };
}

const circle = new Circle(5);
const square = { name: "Square", area: 25 };
const summary = summarize(circle, square, { name: "Triangle", area: 12 });

// ----- Template Literals, Optional Chaining, Nullish Coalescing -----
const message = `Shape: ${circle.name}, Area: ${circle.area()?.toFixed(2) ?? "N/A"}`;
console.log(message);

// ----- Loops, Conditionals, Arrays, Maps -----
for (const color of colors) {
  if (color === "green") continue;
  console.log(`Color: ${color}`);
}

const map = new Map([
  ["Circle", circle],
  ["Square", square]
]);

for (const [key, shape] of map.entries()) {
  console.log(`Key: ${key}, Area: ${shape.area}`);
}

// ----- Exception Handling -----
try {
  circle.radius = -10;
} catch (e) {
  console.warn("Caught error:", e.message);
}

// ----- Modules, Promises, and Lambdas -----
Promise.resolve(42)
  .then(n => n * 2)

