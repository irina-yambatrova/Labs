#include <SFML/Graphics.hpp>
#include <iostream> 
#include <windows.h>

using namespace sf;
using namespace std;

Vector2f WINDOW_SIZE = { 600, 600 };

void Establish_Position_Figure(ConvexShape &convex) { 
	convex.setOrigin(140, 30);
	convex.setPosition(400, 155);
	convex.setFillColor(Color::White);
}

void Set_Pendulum(ConvexShape &fastener, ConvexShape &cargo) { 

	fastener.setPointCount(4);
	fastener.setPoint(0, Vector2f(130, 30)); 
	fastener.setPoint(1, Vector2f(190, 90));
	fastener.setPoint(2, Vector2f(130, 30));
	fastener.setPoint(3, Vector2f(75, 100)); 
	Establish_Position_Figure(fastener);

	cargo.setPointCount(3);
	cargo.setPoint(0, Vector2f(130, 30)); 
	cargo.setPoint(1, Vector2f(160, 400));
	cargo.setPoint(2, Vector2f(130, 400));
	Establish_Position_Figure(cargo);
}

void Set_Gears(Sprite &VinousGearSprite, Sprite &GreenGearSprite) { 
	VinousGearSprite.setPosition(182, 180);
	VinousGearSprite.setOrigin(105, 105);
	GreenGearSprite.setPosition(306, 288);
	GreenGearSprite.setOrigin(99, 98);
}

void Move_pendulum(ConvexShape &fastener, ConvexShape &cargo, float &speed, float &acceleration, float &rotation_pendulum, float &rotation_gear, bool &downhill) { 
	fastener.setRotation(rotation_pendulum);
	cargo.setRotation(rotation_pendulum);
	if (int(speed * 900) == 0) {
		speed = acceleration * 5;
		downhill = true;
	}
	if (int(rotation_pendulum) == 0 && downhill) {
		if (speed > 0)
			rotation_gear -= acceleration;
		speed += acceleration * 10;
		acceleration = -acceleration;
		downhill = false;
	}
	rotation_gear += acceleration * 100;
	speed += acceleration;
	rotation_pendulum += speed;
}

void start_move(RenderWindow &window, Sprite VinousGearSprite, Sprite GreenGearSprite) {
	float rotation_pendulum = 40;
	float rotation_gear = 0;
	float speed = -0.0006f;
	float acceleration = -0.0006f;
	bool downhill = true;

	ConvexShape fastener;
	ConvexShape cargo;
	Set_Gears(VinousGearSprite, GreenGearSprite);
	Set_Pendulum(fastener, cargo);

	while (window.isOpen()) {
		Event event;

		while (window.pollEvent(event)) {
			if (event.type == Event::Closed)
				window.close();
		}
		GreenGearSprite.setRotation(rotation_gear);
		VinousGearSprite.setRotation(-rotation_gear);
		Move_pendulum(fastener, cargo, speed, acceleration, rotation_pendulum, rotation_gear, downhill);

		window.clear();
		window.draw(fastener);
		window.draw(cargo);
		window.draw(VinousGearSprite);
		window.draw(GreenGearSprite);
		window.display();
	}
}

int main() {
	ContextSettings settings;
	settings.antialiasingLevel = 8;

	Texture VinousGearSpriteTexture, GreenGearSpriteTexture;
	VinousGearSpriteTexture.loadFromFile("1.png");
	GreenGearSpriteTexture.loadFromFile("2.png");

	Sprite VinousGearSprite, GreenGearSprite;
	VinousGearSprite.setTexture(VinousGearSpriteTexture);
	GreenGearSprite.setTexture(GreenGearSpriteTexture);

	RenderWindow window(VideoMode(unsigned int(WINDOW_SIZE.x), unsigned int(WINDOW_SIZE.y)), "Pendulum", Style::Default, settings);
	start_move(window, VinousGearSprite, GreenGearSprite);
	return 0;
}
