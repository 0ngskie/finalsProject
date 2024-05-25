class User {
    constructor(UserID, FirstName, LastName, PhoneNumber, Email, Address, UserType) {
        this.UserID = UserID;
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.PhoneNumber = PhoneNumber;
        this.Email = Email;
        this.Address = Address;
        this.UserType = UserType;
    }
  }
  
  module.exports = User;