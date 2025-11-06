from fastapi import APIRouter

router = APIRouter()

# База нормо-часов и материалов (можно расширять)
DATA = {
    "bumper_front": {"hours": 5.5, "materials": 80, "name": "Передний бампер"},
    "bumper_rear": {"hours": 5.0, "materials": 80, "name": "Задний бампер"},
    "door_front": {"hours": 6.5, "materials": 90, "name": "Передняя дверь"},
    "door_rear": {"hours": 6.0, "materials": 90, "name": "Задняя дверь"},
    "fender_front": {"hours": 4.0, "materials": 70, "name": "Переднее крыло"}
}

LABOR_RATE = 55      # €/час
PAINT_COST = 120     # добавка за покраску

@router.get("/estimate")
def estimate(part: str, paint: bool = True):
    if part not in DATA:
        return {"error": "Unknown part"}

    info = DATA[part]

    price_work = info["hours"] * LABOR_RATE
    price_materials = info["materials"]
    price_paint = PAINT_COST if paint else 0

    total = price_work + price_materials + price_paint

    return {
        "detail": info["name"],
        "hours": info["hours"],
        "labor_rate": LABOR_RATE,
        "materials": price_materials,
        "paint_cost": price_paint,
        "total": round(total, 2)
    }
