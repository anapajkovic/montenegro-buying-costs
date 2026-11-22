"""Montenegro resale transfer tax: 3% to EUR 150,000, 5% to EUR 500,000, 6% above (progressive)."""
import sys

BANDS = [(150_000, 0.03), (500_000, 0.05), (float("inf"), 0.06)]


def transfer_tax(price):
    tax, lower, rows = 0.0, 0, []
    for upper, rate in BANDS:
        part = max(0, min(price, upper) - lower)
        if part:
            rows.append((lower, min(price, upper), rate, part * rate))
            tax += part * rate
        lower = upper
    return round(tax), rows


if __name__ == "__main__":
    price = float(sys.argv[1].replace(",", "").replace("€", ""))
    total, rows = transfer_tax(price)
    for lo, hi, rate, amount in rows:
        print(f"EUR {lo:,.0f} - {hi:,.0f} at {rate:.0%}: EUR {amount:,.0f}")
    print(f"Transfer tax on a EUR {price:,.0f} resale: EUR {total:,.0f}")
    print("New build from a developer: no transfer tax (21% VAT is in the price).")
