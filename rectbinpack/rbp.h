struct RectSize {
	int width;
	int height;
	int id;
};

struct Rect {
	int x;
	int y;
	int width;
	int height;
	int id;
};

void MaxRects_init(int width, int height, bool flip);
struct Rect MaxRects_insertOne(int width, int height);
unsigned int MaxRects_insert(struct RectSize *sizes, int num, struct Rect **out);
float MaxRects_occupancy();
