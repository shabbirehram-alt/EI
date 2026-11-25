import asyncio, json, os, edge_tts
items = json.load(open('raabta/lines.json', encoding='utf-8'))
os.makedirs('raabta/vo', exist_ok=True)
async def one(i, t, sem):
    async with sem:
        for attempt in range(4):
            try:
                await edge_tts.Communicate(t, 'ur-PK-AsadNeural', rate='+0%').save(f'raabta/vo/{i:03d}.mp3'); return
            except Exception as e:
                print('retry', i, e); await asyncio.sleep(3)
async def main():
    sem = asyncio.Semaphore(6)
    await asyncio.gather(*[one(i, x['text'], sem) for i, x in enumerate(items)])
asyncio.run(main())
print(len(os.listdir('raabta/vo')))
