let car 

function Car(color, model, year) {
    if(car instanceof Car) {
        return car
    } 

    car = this
    this.color = color
    this.model = model
    this.year = year 
}

const car1 = new Car("black", "suzuki", 189545)
const car2 = new Car("yellow", "bmw", 1954)


console.log(car1, car2)

console.log(Number("43443skdjfa"))