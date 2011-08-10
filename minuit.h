// minuit.h is Copyright (C) 2007 Jim Pivarski <jpivarski@gmail.com>
// See http://seal.web.cern.ch/seal/snapshot/work-packages/mathlibs/minuit/
// for more information about SEAL Minuit 1.7.9.
// 
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
// 
// Full licence is in the file COPYING and at http://www.gnu.org/copyleft/gpl.html

#include <Python.h>
#include <structmember.h>
#include <vector>
#include <sstream>
#include "Minuit/FCNBase.h"
#include "Minuit/MnUserParameters.h"
#include "Minuit/MnUserParameterState.h"
#include "Minuit/MinuitParameter.h"
#include "Minuit/MnSimplex.h"
#include "Minuit/MnMigrad.h"
#include "Minuit/FunctionMinimum.h"
#include "Minuit/MnHesse.h"
#include "Minuit/MnMinos.h"
#include "Minuit/MnCross.h"
#include "Minuit/MnContours.h"
#include "Minuit/ContoursError.h"

#ifndef PyMODINIT_FUNC
#define PyMODINIT_FUNC void
#endif

class ExceptionDuringMinimization {
   public:
      ExceptionDuringMinimization() {}
      ~ExceptionDuringMinimization() {}
};

class MyFCN: public FCNBase {
   public:
      MyFCN(PyObject *fcn, PyObject *self, int npar): m_fcn(fcn), m_self(self), m_npar(npar) { };
      double operator()(const std::vector<double>& par) const;

      double up() const { return m_up; }
      void setUp(double up) { m_up = up; }
      void setPrintMode(int printMode) { m_printMode = printMode; }
      void setOriginal(std::vector<double> par) { m_original = par; }
      
   private:
      PyObject *m_fcn;
      PyObject *m_self;
      int m_npar;
      double m_up;
      int m_printMode;
      std::vector<double> m_original;
};

typedef struct {
      PyObject_HEAD

      MyFCN *myfcn;
      MnUserParameters *upar;
      FunctionMinimum *min;
      int scandepth;

      int npar;
      PyObject *maxcalls;
      double tol;
      int strategy;
      double up;
      int printMode;
      PyObject *fixed;
      PyObject *limits;
      PyObject *values;
      PyObject *args;
      PyObject *errors;
      PyObject *merrors;
      PyObject *covariance;

      PyObject *fcn;
      PyObject *self;
      PyObject *fval;
      int ncalls;
      PyObject *edm;
      PyObject *parameters;
} minuit_Minuit;

static int minuit_Minuit_init(minuit_Minuit* self, PyObject* args, PyObject* kwds);
static int minuit_Minuit_dealloc(minuit_Minuit* self);
bool minuit_prepare(minuit_Minuit *self, int &maxcalls, std::vector<std::string> &floating);
static PyObject* minuit_Minuit_simplex(minuit_Minuit* self);
static PyObject* minuit_Minuit_migrad(minuit_Minuit* self);
static PyObject* minuit_Minuit_hesse(minuit_Minuit* self);
static PyObject* minuit_Minuit_minos(minuit_Minuit* self, PyObject* args);
static PyObject* minuit_Minuit_contour(minuit_Minuit* self, PyObject* args, PyObject* kwds);
static PyObject* minuit_Minuit_scan(minuit_Minuit* self, PyObject* args, PyObject* kwds);
static PyObject* minuit_Minuit_matrix(minuit_Minuit* self, PyObject* args, PyObject* kwds);
static PyObject* minuit_machine_precision();
