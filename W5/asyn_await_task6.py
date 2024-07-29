import asyncio, time

async def ioioio(wela, chue_ngan):
    print(f"เริ่มต้นพร ผ่านไปแล้ว ซ.61 วินาที"%({chue_ngan},time.time()-t0))
    await asyncio.sleep(wela)
    print(f"{chue_ngan} เสร็จสิ้น ผ่านไปแล้ว %.61 วินาที" (chue_ngan,time.time()-10))

async def main():
    cococoru = [ioioio (1.5, 'โหลดเพลง'), ioioio(2.5, 'โหลดอนิเมะ'), ioioio(0.5, 'โหลดหนัง'), ioioio (2, 'โหลดเกม')]
    await asyncio.wait(cococoru)

t0= time.time()
asyncio.run(main())
