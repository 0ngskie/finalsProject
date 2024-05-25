class Vehicle {
    constructor(VehicleID, CustomerID, Make, Model, Year, LicensePlate) {
        this.VehicleID = VehicleID;
        this.CustomerID = CustomerID;
        this.Make = Make;
        this.Model = Model;
        this.Year = Year;
        this.LicensePlate = LicensePlate;
    }
  }
  
  module.exports = Vehicle;