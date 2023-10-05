class LiquidityPool {
  constructor(tokenA, tokenB) {
    this.tokenA = tokenA
    this.tokenB = tokenB
  }

  getPriceOfTokenA() {
    return this.tokenB / this.tokenA;
  }
  getPriceOfTokenB() {
    return this.tokenA / this.tokenB;
  }

  buyTokenA(amountB) {
    let amountA = amountB / this.getPriceOfTokenA();
    this.tokenA -= amountA;
    this.tokenB += amountB;
  }
  buyTokenB(amountA) {
    let amountB = amountA / this.getPriceOfTokenB()
    this.tokenB -= amountB
    this.tokenA += amountA
  }
  
  displayPool() {
    const poolData = {
      'tokenA balance': this.tokenA.toLocaleString(),
      'tokenB balance': this.tokenB.toLocaleString(),
      'tokenA price': this.getPriceOfTokenA().toLocaleString(),
      'tokenB price': this.getPriceOfTokenB().toLocaleString()
    };
    console.table(poolData);
  }

  /*displayPool() {
    const values = `
    tokenA balance: ${this.tokenA.toLocaleString()}
    tokenB balance: ${this.tokenB.toLocaleString()}
    tokenA price: ${this.getPriceOfTokenA().toLocaleString()}
    tokenB price: ${this.getPriceOfTokenB().toLocaleString()}`
    console.log(values)
  }*/
}

function main() {
  const p = new LiquidityPool(1000, 1000)
  for(let i = 0; i < 100; i++) {
    let purchasingA = Math.random() < 0.5
    let purchaseAmount = Math.floor(Math.random() * 100)
    if(purchasingA){
      console.log(`Buying ${purchaseAmount} tokenA for ${p.getPriceOfTokenA() * purchaseAmount} tokenB`)
      p.buyTokenA(purchaseAmount)
    } else {
      console.log(`Buying ${purchaseAmount} tokenB for ${p.getPriceOfTokenB() * purchaseAmount} tokenA`)
      p.buyTokenB(purchaseAmount)
    }
    p.displayPool()
  }
}

main()