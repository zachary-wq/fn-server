import asyncio
import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse


router = APIRouter(
    tags=["sse"],
    prefix="/sse",
)

async def fake_video_streamer():
    for i in range(10):
        yield f"data: {json.dumps({"tmp": i})}\n\n"
        await asyncio.sleep(1)

@router.get("/test")
async def test_sse():
    return StreamingResponse(fake_video_streamer(), media_type="text/event-stream")