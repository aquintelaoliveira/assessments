package banking;

/**
 *
 * Private Variables:<br>
 * {@link #accountNumber}: Long<br>
 * {@link #bank}: Bank<br>
 */
public class Transaction implements TransactionInterface{ // TODO: MISSING implements
	private Long accountNumber;
	private Bank bank;

	/**
	 *
	 * @param bank
	 *            The bank where the account is housed.
	 * @param accountNumber
	 *            The customer's account number.
	 * @param attemptedPin
	 *            The PIN entered by the customer.
	 * @throws Exception
	 *             Account validation failed.
	 */
	public Transaction(Bank bank, Long accountNumber, int attemptedPin) throws Exception {
		if(!bank.authenticateUser(accountNumber, attemptedPin)) {
			throw new Exception("Wrong pin");
		}
		this.bank = bank;
		this.accountNumber = accountNumber;
	}

	public double getBalance() {
		return this.bank.getBalance(accountNumber);
	}

	public void credit(double amount) {
		this.bank.credit(this.accountNumber, amount);
	}

	public boolean debit(double amount) {
		return this.bank.debit(accountNumber, amount);
	}
}
