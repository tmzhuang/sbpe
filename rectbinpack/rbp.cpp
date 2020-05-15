#include "MaxRectsBinPack.h"
#include <vector>

using namespace rbp;

MaxRectsBinPack mbp;

std::vector<Rect> dst;

extern "C" {

void MaxRects_init(int width, int height, bool flip) {
    mbp.Init(width, height, flip);
}

struct Rect MaxRects_insertOne(int width, int height) {
	return mbp.Insert(width, height, MaxRectsBinPack::RectBestShortSideFit);
}

unsigned int MaxRects_insert(struct RectSize *sizes, int num, struct Rect **out) {
	std::vector<RectSize> rects(sizes, sizes + num);
	mbp.Insert(rects, dst, MaxRectsBinPack::RectBestShortSideFit);
	*out = dst.data();
	return dst.size();
}

float MaxRects_occupancy() {
	return mbp.Occupancy();
}

}
