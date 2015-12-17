
#include <iostream>
#include <SFML/Graphics.hpp>
#include <windows.h>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace sf;
const int WINDOW_X = 440;
const int WINDOW_Y = WINDOW_X;
const int START_X = WINDOW_X / 2;
const int START_Y = WINDOW_Y / 2;
const int AMOUNT_POINTS = 60;
const int SCALE = 175;


struct Shapes {
	ConvexShape secArrow;
	ConvexShape minArrow;
	ConvexShape hourArrow;
	CircleShape centre;
	CircleShape point;
}watch;


void CalculateCoordinates(std::vector<Vector2f> & points) {
	points.resize(AMOUNT_POINTS);
	for (int i = 0; i < AMOUNT_POINTS; i++) {
		points[i].x = START_X + SCALE * cos(i * 6 * float(M_PI) / 180);
		points[i].y = START_Y + SCALE * sin(i * 6 * float(M_PI) / 180);
	}
}

void DrawPoints(RenderWindow &window, std::vector<Vector2f> const& points) {
	for (int i = 0; i < AMOUNT_POINTS; i++) {
		if (i % 15 == 0) {
			watch.point.setRadius(6);
			watch.point.setOrigin(6 / 2, 6 / 2);
			watch.point.setFillColor(Color::Blue);
		}
		else if (i % 5 == 0) {
			watch.point.setRadius(4);
			watch.point.setOrigin(4 / 2, 4 / 2);
			watch.point.setFillColor(Color::Blue);
		}
		else {
			watch.point.setRadius(1);
			watch.point.setOrigin(1 / 2, 1 / 2);
			watch.point.setFillColor(Color::Blue);
		}
		watch.point.setPosition(points[i]);
		window.draw(watch.point);
	}
}

void PositionOneArrow(ConvexShape &arrow, float height, float width) {
	arrow.setPointCount(3);
	arrow.setPoint(0, sf::Vector2f(0, 0));
	arrow.setPoint(1, sf::Vector2f(width / 2, -height));
	arrow.setPoint(2, sf::Vector2f(width, 0));
	arrow.setPosition(float(START_X), float(START_Y));
	arrow.setOrigin(width / 2, -height / 8);
}

void PositionArrows() {
	PositionOneArrow(watch.hourArrow, 130, 14);
	watch.hourArrow.setFillColor(Color::Black);
	PositionOneArrow(watch.minArrow, 145, 10);
	watch.minArrow.setFillColor(Color::Black);
	PositionOneArrow(watch.secArrow, 160, 8);
	watch.secArrow.setFillColor(Color::Red);

	watch.centre.setRadius(6);
	watch.centre.setFillColor(Color::Black);
	watch.centre.setPosition((WINDOW_X / 2) - watch.centre.getRadius(), (WINDOW_Y / 2) - watch.centre.getRadius());
}
void DrawHours(RenderWindow &window, std::vector<Vector2f> const& points)
{
	
	window.draw(watch.hourArrow);
	window.draw(watch.minArrow);
	window.draw(watch.secArrow);
	window.draw(watch.centre);
	DrawPoints(window, points);
}

void TimeIsOn(RenderWindow &window)
{
	PositionArrows();
	std::vector<Vector2f> points;
	CalculateCoordinates(points);
	SYSTEMTIME sysTime;
	while (window.isOpen())
	{
		Event event;
		while (window.pollEvent(event))
		{
			if (event.type == Event::Closed)
				window.close();
		}

		GetSystemTime(&sysTime);
		watch.secArrow.setRotation(float(sysTime.wSecond * 360 / 60));
		watch.minArrow.setRotation(float(sysTime.wMinute * 360 / 60 + sysTime.wSecond * 6 / 60));
		watch.hourArrow.setRotation(float((sysTime.wHour + 3) * 30 + (sysTime.wMinute * 30 / 60)));

		window.clear(Color::White);
		DrawHours(window, points);
		window.display();

	}
}
int main()
{
	ContextSettings settings;
	settings.antialiasingLevel = 8;
	RenderWindow window(VideoMode(WINDOW_X, WINDOW_Y), "Clock", sf::Style::Default, settings);
	TimeIsOn(window);
	return 0;
}