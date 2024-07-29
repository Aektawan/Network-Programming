import asyncio, time

async def ioioio(wela, chue_ngan):
    print(f"เริ่ม%s เวลาผ่านไปแล้ว %.5f วินาที" (chue_ngan, time.time() - t0))
    await asyncio.sleep(wela)
    print(f"{chue_ngan} เสร็จแล้ว เวลาผ่านไปแล้ว %.51 วินาที (time.time() - t0)")
    return

async def main():
    print("Started Function")
    phara1 = asyncio.create_task(ioioio(1.5, "Downloading Music"))
    phara2 = asyncio.create_task(ioioio(2.5, "Downloading Anime"))
    phara3 = asyncio.create_task(ioioio(0.5, "Downloading Movie"))
    print("Mission Created")
    await phara2
    print("Mission Complete")

t0 = time.time()
asyncio.run(main())
