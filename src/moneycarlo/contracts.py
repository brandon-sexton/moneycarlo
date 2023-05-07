from datetime import datetime


class Contract:
    def __init__(self, pwin: float, value: float, award_date: datetime) -> None:
        self.probability_of_win: float = pwin
        self.value: float = value
        self.award_date: datetime = award_date

    @classmethod
    def from_csv_line(cls, line: str) -> "Contract":
        contents: list = line.split(",")
        year: int = int(contents[0])
        month: int = 3 * int(contents[1])
        pwin: float = 0.0
        if contents[2] == "low":
            pwin = 0.25
        elif contents[2] == "medium":
            pwin = 0.5
        elif contents[2] == "high":
            pwin = 0.75
        elif contents[2] == "won":
            pwin = 1.0

        val: float = float(contents[3])
        return cls(pwin, val, datetime(year, month, 1))


class RevenuePlan:
    def __init__(self) -> None:
        self.contracts: list[Contract] = []

    @classmethod
    def from_csv(cls, contracts_csv_name: str) -> "RevenuePlan":

        plan: RevenuePlan = cls()

        with open(contracts_csv_name, "r") as f:
            lines = f.readlines()

        for line in lines[1:]:
            plan.contracts.append(Contract.from_csv_line(line))

        return plan
