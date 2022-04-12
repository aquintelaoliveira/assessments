package banking;

public class Person extends AccountHolder {
	private String firstName;
	private String lastName;

	public Person(String firstName, String lastName, int idNumber) {
		super(idNumber);
		this.firstName = firstName;
		this.lastName = lastName;
	}

	public String getFirstName() {
		return this.firstName;
	}

	public String getLastName() {
		return this.lastName;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		Person person = (Person) o;
		return firstName.equals(person.firstName) && lastName.equals(person.lastName) && getIdNumber() == person.getIdNumber();
	}
}
