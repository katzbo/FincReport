describe('get expenses list in Leumi bank', function() {
  it('get expenses list', function() {

    browser.ignoreSynchronization = true;

    browser.get('https://www.leumi.co.il');
    var login = element.all(by.className('includeLink'));
    login.get(0).click();
    element(by.id('uid')).sendKeys("username");
    element(by.id('password')).sendKeys("password");
    element(by.id('enter')).click();
  });
});