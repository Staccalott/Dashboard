import React from 'react';
import { Container, Row, Col, Card, Table, Nav, Navbar } from 'react-bootstrap';
import { HouseDoor, Book, People, CurrencyDollar, List } from 'react-bootstrap-icons';

const AdminDashboard = () => {
  return (
    <div style={{ fontFamily: "'Poppins', sans-serif", backgroundColor: "#f8f9fa", minHeight: "100vh" }}>
      <Row className="g-0">
        {/* Sidebar */}
        <Col md={2} className="bg-white border-end vh-100 d-none d-md-block position-fixed">
          <div className="p-4">
            <h4 className="text-primary fw-bold mb-5">AdminFlow</h4>
            <Nav className="flex-column gap-2">
              <Nav.Link href="#" className="bg-primary text-white rounded-3 p-3 d-flex align-items-center gap-2">
                <HouseDoor /> Dashboard
              </Nav.Link>
              <Nav.Link href="#" className="text-secondary p-3 d-flex align-items-center gap-2 hover-light">
                <Book /> Courses
              </Nav.Link>
              <Nav.Link href="#" className="text-secondary p-3 d-flex align-items-center gap-2">
                <People /> Students
              </Nav.Link>
              <Nav.Link href="#" className="text-secondary p-3 d-flex align-items-center gap-2">
                <CurrencyDollar /> Revenue
              </Nav.Link>
            </Nav>
          </div>
        </Col>

        {/* Main Content Area */}
        <Col md={{ span: 10, offset: 2 }} className="p-4">
          <header className="mb-4">
            <small className="text-muted">Pages / Dashboard</small>
            <h2 className="fw-bold text-dark">Main Dashboard</h2>
          </header>

          {/* Stats Cards */}
          <Row className="mb-4">
            {[
              { title: 'Total Courses', val: '34', icon: <Book />, color: 'primary' },
              { title: 'Total Students', val: '2,450', icon: <People />, color: 'info' },
              { title: 'Revenue', val: '$12,800', icon: <CurrencyDollar />, color: 'success' }
            ].map((stat, idx) => (
              <Col md={4} key={idx}>
                <Card className="border-0 shadow-sm rounded-4 p-3">
                  <Card.Body className="d-flex align-items-center gap-3">
                    <div className={`bg-${stat.color} bg-opacity-10 p-3 rounded-circle text-${stat.color} fs-4`}>
                      {stat.icon}
                    </div>
                    <div>
                      <Card.Subtitle className="text-muted mb-1 small">{stat.title}</Card.Subtitle>
                      <Card.Title className="fw-bold mb-0 fs-4">{stat.val}</Card.Title>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
            ))}
          </Row>

          {/* Recent Enrollments Table */}
          <Card className="border-0 shadow-sm rounded-4">
            <Card.Body className="p-4">
              <Card.Title className="fw-bold mb-4">Recent Enrollments</Card.Title>
              <Table responsive borderless className="align-middle">
                <thead>
                  <tr className="text-muted small border-bottom">
                    <th className="pb-3">COURSE NAME</th>
                    <th className="pb-3">STUDENT</th>
                    <th className="pb-3">DATE</th>
                    <th className="pb-3">STATUS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-bottom">
                    <td className="py-3 fw-bold">Fullstack Web Development</td>
                    <td className="py-3 text-secondary">James Smith</td>
                    <td className="py-3 text-secondary">Jan 12, 2026</td>
                    <td className="py-3">
                      <span className="badge bg-success-subtle text-success rounded-pill px-3 py-2">Completed</span>
                    </td>
                  </tr>
                  <tr>
                    <td className="py-3 fw-bold">UI/UX Design Masterclass</td>
                    <td className="py-3 text-secondary">Sarah Connor</td>
                    <td className="py-3 text-secondary">Jan 15, 2026</td>
                    <td className="py-3">
                      <span className="badge bg-warning-subtle text-warning rounded-pill px-3 py-2">Pending</span>
                    </td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default AdminDashboard;