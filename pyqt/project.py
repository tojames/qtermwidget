from pyqtbuild import PyQtBindings, PyQtProject
import os
import pathlib

class QTermWidget(PyQtProject):
    def __init__(self):
        super().__init__()
        self.bindings_factories = [QTermWidgetBindings]

class QTermWidgetBindings(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, name='QTermWidget', sip_file='qtermwidget.sip', qmake_QT=['widgets'])

    def apply_user_defaults(self, tool):
        # TODO: use an SIP build option
        build_dir = pathlib.Path(os.environ['QTERMWIDGET_BUILD_DIR']).resolve()
        self.include_dirs.append(pathlib.Path(__file__).resolve().parents[1] / 'lib')
        self.include_dirs.append(build_dir / 'lib')
        self.library_dirs.append(build_dir)
        self.libraries.append('qtermwidget5')

        super().apply_user_defaults(tool)
