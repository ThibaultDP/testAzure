resource appServicePlan 'Microsoft.Web/serverfarms@2021-02-01' = {
  name: 'mywebappserviceplan'
  location: 'global'
  sku: {
    name: 'B1'
    tier: 'Basic'
  }
}

resource webApp 'Microsoft.Web/sites@2021-02-01' = {
  name: 'mywebapp'
  location: 'global'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'PYTHON_VERSION', value: '3.8'
        }
      ]
    }
  }

}
