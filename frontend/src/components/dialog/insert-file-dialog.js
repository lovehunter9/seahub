import React from 'react';
import PropTypes from 'prop-types';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter, Alert } from 'reactstrap';
import { gettext } from '../../utils/constants';
import { Utils } from '../../utils/utils';
import FileChooser from '../file-chooser/file-chooser';
import '../../css/dirent-detail.css';

const propTypes = {
  repoID: PropTypes.string.isRequired,
  filePath: PropTypes.string.isRequired,
  toggleCancel: PropTypes.func.isRequired,
  dirent: PropTypes.object.isRequired,
  getInsertLink: PropTypes.func.isRequired,
};

class InsertFileDialog extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      repo: null,
      selectedPath: '',
    };
  }

  handleInsert = () => {
    this.props.getInsertLink(this.state.repo.repo_id, this.state.selectedPath);
    this.props.toggleCancel();
  }

  onDirentItemClick = (repo, selectedPath, dirent) => {
    if (dirent.type === 'file') {
      this.setState({
        repo: repo,
        selectedPath: selectedPath,
      });
    }
    else {
      this.setState({
        repo: null,
        selectedPath: '',
      });
    }
  }

  onRepoItemClick = () => {
    this.setState({
      repo: null,
      selectedPath: '',
    });
  }

  render() {
    let subtitle = gettext('Insert file in {placeholder}');
    subtitle = subtitle.replace('{placeholder}', '<span class="op-target">' + Utils.HTMLescape(this.props.dirent.name) + '</span>');
    const toggle = this.props.toggleCancel;
    return (
      <Modal isOpen={true} className="sf-add-related-file" toggle={toggle} >
        <ModalHeader toggle={toggle}>{gettext('Select File')}</ModalHeader>
        <ModalBody>
          <div className="related-file-subtitle" dangerouslySetInnerHTML={{__html: subtitle}}></div>
          <FileChooser
            isShowFile={true}
            repoID={this.props.repoID}
            onDirentItemClick={this.onDirentItemClick}
            onRepoItemClick={this.onRepoItemClick}
            mode="current_repo_and_other_repos"
          />
        </ModalBody>
        <ModalFooter>
          <Button color="secondary" onClick={toggle}>{gettext('Cancel')}</Button>
          {this.state.selectedPath ? <Button color="primary" onClick={this.handleInsert}>{gettext('Insert')}</Button>
            : <Button color="primary" disabled>{gettext('Insert')}</Button>}
        </ModalFooter>
      </Modal>
    );
  }
}

InsertFileDialog.propTypes = propTypes;

export default InsertFileDialog;
