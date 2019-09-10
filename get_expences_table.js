var fs = require("fs");

describe("get expenses list in Leumi bank", function() {
    it("get expenses list", function() {
        browser.ignoreSynchronization = true;

        browser.get("https://www.leumi.co.il");
        var login = element.all(by.className("includeLink"));
        login.get(0).click();
        element(by.id("uid")).sendKeys("username");
        element(by.id("password")).sendKeys("password");
        element(by.id("enter")).click();

        var elem = element(by.className("credit-card-directive-template"));
        var page_sections = elem.all(by.className("row"));
        page_sections.count().then(function(count) {
            console.log(count);
        });
        var cards = page_sections
            .get(2)
            .all(
                by.repeater(
                    "item in vm.userDataService.model.selectedAccount.responses['SO_GetCreditCardData'].data.CreditCardItems | limitTo:4"
                )
            );
        cards.count().then(function(count) {
            console.log(count);
        });

        browser.wait(
            protractor.ExpectedConditions.elementToBeClickable(cards.get(0)),
            5000,
            "Element not clickable"
        );
        cards.get(0).click();

        browser.wait(
            protractor.ExpectedConditions.elementToBeClickable(
                element(by.className("credit-card-activity-tpl"))
            ),
            5000,
            "Element not clickable"
        );
        var expenses_table = element(by.className("credit-card-activity-tpl"));
        var expenses = expenses_table.all(
            by.className("cc-table-entry expand-item")
        );
        expenses.count().then(function(count) {
            console.log(count);
        });

        // get necessary information from expenses (business name, amount)
        var expensesToFile = expenses.map(async function(elem, index) {
            return {
                name: elem
                    .element(by.className("ts-table-row-item u-flex-grow2"))
                    .getText(),
                amount: elem
                    .element(
                        by.className(
                            "ts-table-row-item d-none d-sm-flex xlcurrencycode-1"
                        )
                    )
                    .getText()
            };
        });
        expensesToFile.then(function (expensesToFile) {
            console.log(expensesToFile);
        });
        fs.writeFileSync("expenses.json", JSON.stringify(expensesToFile));
    });
});

