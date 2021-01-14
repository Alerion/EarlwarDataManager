import buildUrl from 'build-url';
import axios from 'axios'


class Api {
  constructor(config) {
    this.basePath = config.basePath;
  }

  tableUrl(queryParams) {
    return buildUrl(this.basePath, {
      path: 'table',
      queryParams,
    });
  }

  treeUrl() {
    return buildUrl(this.basePath, {
      path: 'tree',
    });
  }

  iconUrl(path) {
    return buildUrl(this.basePath, {
      path: `icon/${path}`
    })
  }

  itemUrl(queryParams) {
    return buildUrl(this.basePath, {
      path: 'edit',
      queryParams,
    });
  }

  abilitiesUrl() {
    const queryParams = {
      path: 'Abilities',
    }
    return buildUrl(this.basePath, {
      path: 'list',
      queryParams,
    });
  }

  table(queryParams) {
    return axios.get(this.tableUrl(queryParams));
  }

  tree() {
    return axios.get(this.treeUrl());
  }

  item(queryParams) {
    return axios.get(this.itemUrl(queryParams));
  }

  abilities() {
    return axios.get(this.abilitiesUrl());
  }
}

export default new Api({
  basePath: process.env.VUE_APP_BACKEND_API,
});